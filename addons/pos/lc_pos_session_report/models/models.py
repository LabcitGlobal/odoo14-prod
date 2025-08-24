# -*- coding: utf-8 -*-

from odoo import models, fields, api, tools
from datetime import date, datetime, time
from dateutil.relativedelta import relativedelta
import pytz

class lc_pos_session_report(models.TransientModel):
      _name = 'lc.pos.session.report'

      def _get_user_id(self):
        user_rec = self.env['res.users'].search([('id', '=', self.env.uid)], limit=1)
        return user_rec.id

      from_date = fields.Datetime('From Date',required=True)
      to_date = fields.Datetime('To Date', required=True)    
      user_id = fields.Many2one('res.users',string="Vendedor", default=_get_user_id)
      delivery_id = fields.Many2one('res.users', string="Chofer")


      def print_session_report(self):
        
        user_tz = pytz.timezone(self.env.context.get('tz') or self.env.user.tz)
        from_date_utc = pytz.utc.localize(self.from_date).astimezone(user_tz)
        to_date_utc = pytz.utc.localize(self.to_date).astimezone(user_tz)
        datas = []        
        total_amount = 0
        total_lists = 0
        
        sql_query = """
            SELECT o.id, o.name AS order_name, o.date_order::timestamp at time zone 'UTC' AS date_order, ROUND(o.amount_total,2) AS amount_total, p.name AS partner_name, p.phone, p.mobile 
            FROM pos_order o 
            LEFT JOIN res_partner p ON o.partner_id=p.id 
            WHERE  o.date_order BETWEEN '%s' AND '%s' AND o.user_id=%s 
            AND o.amount_total>0 
            AND o.name NOT IN(SELECT * FROM lc_posorderrefund_view) 
            ORDER BY p.name, o.id;
        """ % (self.from_date,self.to_date,self.user_id.id)
        
        self.env.cr.execute(sql_query)
        result = self.env.cr.dictfetchall()        
        for reg in result:              
            datas.append({
                'order_id':reg['id'],
                'order_name': reg['order_name'],                
                'date_order':reg['date_order'],
                'amount_total':reg['amount_total'],
                'partner_name':reg['partner_name'],
                'partner_phone':reg['phone'],
                'partner_mobile':reg['mobile'],                
            })
            total_amount += reg['amount_total']
            total_lists += 1            

        res = {
            'orders':datas,            
            'from_date': from_date_utc,
            'to_date': to_date_utc,            
            'employee': self.user_id.partner_id.name,
            'total_amount': round(total_amount,2),
            'total_lists': total_lists,
            'delivery_user': self.delivery_id.partner_id.name,            
        }
        data = {
            'form': res,
        }
        return self.env.ref('lc_pos_session_report.lc_pos_session_report_print').report_action([],data=data)

class LcPosOrderView(models.Model):
    _name = "lc.posorderrefund.view"
    _auto = False
     
    def init(self):        
        tools.drop_view_if_exists(self._cr, 'lc_posorderrefund_view')        
        self._cr.execute("""        
            CREATE or REPLACE VIEW lc_posorderrefund_view AS (
                SELECT 
                SUBSTR(name,1,POSITION('REEMBOLSO' IN name)-1) AS name 
                FROM pos_order 
                WHERE name LIKE '%REEMBOLSO%'                                
            )""")