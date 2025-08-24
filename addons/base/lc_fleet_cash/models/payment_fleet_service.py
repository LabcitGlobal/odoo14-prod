# -*- coding: utf-8 -*-

from num2words import num2words
from odoo import models, fields, api

class LccashFleetService(models.Model):     
    _inherit = 'lccash.payment'

    def amount_to_tex(self,mount):
        return num2words(mount,lang='es')
          
    fleet_service_id = fields.Many2one('lc.fleet.service', string="Service")    
    
    @api.onchange('fleet_service_id')
    def _onchange_fleet_service(self):
        self.mount = self.fleet_service_id.amount
        self.paid = self.fleet_service_id.amount

    @api.model
    def create(self,values):
        val = {}        
        payment_line = self.env['lccash.payment'].search([('fleet_service_id','=',values['fleet_service_id'])])
        payment_total = sum(payline.paid for payline in payment_line)
        val['payment'] = payment_total + values['paid']               
        fleet_service_record = self.env['lc.fleet.service'].search([('id','=',values['fleet_service_id'])])
        fleet_service_record.write(val)
        record = super(LccashFleetService, self).create(values)
        return record
        
    def write(self,values):
        val = {}
        payment_ok = self.env['lccash.payment'].search([('id','=',self.id)])
        payment_line = self.env['lccash.payment'].search([('fleet_service_id','=',self.fleet_service_id.id)])
        payment_total = sum(payline.paid for payline in payment_line) 
        if 'paid' in values:
            val['payment'] = payment_total - payment_ok['paid'] + values['paid']                                
        pos_record = self.env['lc.fleet.service'].search([('id','=',self.fleet_service_id.id)])
        pos_record.write(val)
        record = super(LccashFleetService, self).write(values)
        return record