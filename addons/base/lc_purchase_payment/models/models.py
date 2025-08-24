# -*- coding: utf-8 -*-

from odoo import models, fields, api

class lcPurchaseOrder(models.Model):     
     _inherit = 'purchase.order'
          
     payment = fields.Float(string='Pagado',compute='_total_payment', store=True)
           
     def _total_payment(self):
         for record in self:                                               
             payment_line = self.env['lccash.withdraw'].search([('purchase_id','=',record.id)])
             record.payment = sum(payline.name for payline in payment_line)
             