# -*- coding: utf-8 -*-

from odoo import models, fields, api

class lc_lccash_payment(models.Model):     
    _inherit = 'lccash.payment'
          
    delivery_id = fields.Many2one('lccommission.agent','Chofer')
    packer_id = fields.Many2one('lccommission.agent','Alistador')
    
    @api.onchange('name')
    def _onchange_name(self):
        self.mount = self.name.amount_total
        self.paid = self.name.amount_total
        self.delivery_id = self.name.delivery_id
        self.packer_id = self.name.packer_id


    @api.model
    def create(self,values):
        val = {}        
        payment_line = self.env['lccash.payment'].search([('name','=',values['name'])])
        payment_total = sum(payline.paid for payline in payment_line)
        val['payment'] = payment_total + values['paid']       
        val['delivery_id'] = values['delivery_id']       
        val['packer_id'] = values['packer_id']
        pos_record = self.env['pos.order'].search([('id','=',values['name'])])
        pos_record.write(val)
        record = super(lc_lccash_payment, self).create(values)
        return record
    
    def write(self,values):
        val = {}
        payment_ok = self.env['lccash.payment'].search([('id','=',self.id)])
        payment_line = self.env['lccash.payment'].search([('name','=',self.name.id)])
        payment_total = sum(payline.paid for payline in payment_line) 
        if 'paid' in values:
            val['payment'] = payment_total - payment_ok['paid'] + values['paid']                        
        if 'delivery_id' in values:
            val['delivery_id'] = values['delivery_id']       
        if 'packer_id' in values:
            val['packer_id'] = values['packer_id']
        pos_record = self.env['pos.order'].search([('id','=',self.name.id)])
        pos_record.write(val)
        record = super(lc_lccash_payment, self).write(values)
        return record