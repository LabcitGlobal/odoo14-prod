# -*- coding: utf-8 -*-

from odoo import models, fields, api, tools
from datetime import date
from pytz import timezone

class lcPosShipmentReport(models.TransientModel):
      _name = 'lc.pos.shipment.report'

      from_date = fields.Date('From Date', default=lambda self:fields.Date.to_string(date.today()),required=True)
      to_date = fields.Date('To Date', default=lambda self: fields.Date.to_string(date.today()), required=True)    
      user_id = fields.Many2one('res.users',string="Vendedor")


      def print_shipment_report(self):
        datas = []        
        total_amount = 0
        total_lists = 0
        
        if self.user_id:
          pos_order = self.env['pos.order'].search([('date_order','>=',self.from_date),('date_order','<=',self.to_date),('destiny','!=',False),('user_id','=',self.user_id.id)])
        else:
          pos_order = self.env['pos.order'].search([('date_order','>=',self.from_date),('date_order','<=',self.to_date),('destiny','!=',False)])        
        for reg in pos_order:              
            datas.append({
                'order_id':reg.id,
                'date_order': reg.date_order,
                'order_name': reg.user_id.name,                
                'date_order':reg.date_order,
                'amount_total':round(reg.amount_total,2),
                'partner_name':reg.partner_id.name,
                'partner_phone':reg.partner_id.phone,
                'partner_mobile':reg.partner_id.mobile,
                'shipping_company':reg.shipping_company.name,
                'shipping_partner':reg.shipping_partner.name,
                'destiny': reg.destiny.name,
                'box_quantity': reg.box_quantity,
                'packer_id':reg.packer_id.name.name,
                'passage':reg.passage,
                'shipping_cost':reg.shipping_cost,
            })
            total_amount += reg.amount_total
            total_lists += 1
        res = {
            'orders':datas,            
            'from_date': self.from_date,
            'to_date': self.to_date,            
            'employee': self.user_id.partner_id.name,
            'total_amount': round(total_amount,2),
            'total_lists': total_lists,            
        }
        data = {
            'form': res,
        }
        return self.env.ref('lc_pos_shipment_report.lc_pos_shipment_report_print').report_action([],data=data)