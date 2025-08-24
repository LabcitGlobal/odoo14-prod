# -*- coding: utf-8 -*-

from odoo import models, fields, api, tools
from datetime import date
from pytz import timezone

class LcSessionMarker(models.TransientModel):
    _name = 'lc.pos.marker'    

    from_date = fields.Date('From Date', default=lambda self:fields.Date.to_string(date.today()),required=True)
    to_date = fields.Date('To Date', default=lambda self: fields.Date.to_string(date.today()), required=True)    
    users_id = fields.Many2many('hr.employee',string="Seller")

    def marker_pos_order(self):

        ids = ''
        for user_id in self.users_id:
            ids = ids + str(user_id.user_id.id) + ','
        ids = ids[:len(ids)-1]
        
        if self.users_id:
          sql_query = """
            update res_partner set marker_color='green' where marker_color!='green' and marker_color!='orange';
            update res_partner set marker_color='red' where id in(
            select distinct partner_id 
            from pos_order 
            where partner_id is not null and DATE(date_order::timestamp at time zone 'UTC') between '%s' and '%s'
            and amount_total>0 
            and name not in(SELECT * FROM lc_posorderrefund_view) 
            and user_id in (%s)
            );
          """ % (self.from_date,self.to_date,ids)
        else:
            sql_query = """
            update res_partner set marker_color='green' where marker_color!='green' and marker_color!='orange';
            update res_partner set marker_color='red' where id in(
            select distinct partner_id 
            from pos_order 
            where partner_id is not null and DATE(date_order::timestamp at time zone 'UTC') between '%s' and '%s'
            and amount_total>0 
            and name not in(SELECT * FROM lc_posorderrefund_view)
            );
            """ % (self.from_date,self.to_date)
        self.env.cr.execute(sql_query)

    def marker_end_pos_order(self):
      
        sql_query = """
        update res_partner set marker_color='green' where marker_color!='green' and marker_color!='orange';            
        """
        self.env.cr.execute(sql_query)