# -*- coding: utf-8 -*-

from odoo import models, fields, api

class lcPosOrder(models.Model):
     _inherit = 'pos.order'
                
     def action_recalculate_margin(self):
         total = 0
         for line in self.lines:
              margin = (line.price_unit - line.product_id.standard_price) * line.qty
              line.purchase_price_backup = line.purchase_price
              line.purchase_price = line.product_id.standard_price
              line.margin = margin
              total += margin
         self.margin = total
     
     def action_restore_margin(self):
         total = 0
         for line in self.lines:
              line.purchase_price = line.purchase_price_backup
              line.purchase_price_backup = 0
              margin = (line.price_unit - line.purchase_price) * line.qty
              line.margin = margin
              total += margin
         self.margin = total

class lcPosOrderLine(models.Model):
     _inherit = 'pos.order.line'

     purchase_price_backup = fields.Float(string='Purchase Price')

        
         