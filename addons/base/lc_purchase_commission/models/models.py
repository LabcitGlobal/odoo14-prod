# -*- coding: utf-8 -*-

from odoo import models, fields, api

class lcPurchaseOrder(models.Model):     
     _inherit = 'purchase.order'
          
     supplier_margin = fields.Float(string='Supplier Margin')
     supplier_margin_percentage = fields.Float(string='Margin Percentage (%)')
     supplier_margin_commission = fields.Float(string='Margin Commission', compute='_compute_margin_commission', store=True)

     @api.depends('supplier_margin','supplier_margin_percentage')      
     def _compute_margin_commission(self):
        for record in self:
            record.supplier_margin_commission = record.supplier_margin * (record.supplier_margin_percentage / 100)