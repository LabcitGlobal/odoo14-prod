# -*- coding: utf-8 -*-

from odoo import models, fields, api

class lc_pos_payment(models.Model):     
     _inherit = 'pos.order'
          
     payment = fields.Float(string='Pagado',compute='_total_payment', store=True)
           
     def _total_payment(self):
         for record in self:                                 
             payment_line = self.env['lccash.payment'].search([('name','=',record.id)])
             record.payment = sum(payline.paid for payline in payment_line)
             