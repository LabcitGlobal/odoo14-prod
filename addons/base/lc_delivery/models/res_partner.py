# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date
from pytz import timezone

class DeliveryPartner(models.Model):
    _inherit = "res.partner"
    
    delivery_count = fields.Integer(string="Delivery", compute='get_delivery_pending')        

    def get_delivery_pending(self):
        count = 0
        pending = self.env['lc.delivery.cost'].search([('name','=',self.id),('company_id','=',self.env.company.id),('state','=','pending')])
        for line in pending:
            count = count + line.mount
        self.delivery_count = count

    def open_delivery_pending(self):
        return {
            'name': 'Delivery Pending',
            'domain': [('name','=',self.id),('company_id','=',self.env.company.id)],            
            'res_model': 'lc.delivery.cost',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }