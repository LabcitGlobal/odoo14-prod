# -*- coding: utf-8 -*-

from odoo import api, fields, models
import odoo.addons.decimal_precision as dp

class lcpurchaseOrderPrices(models.Model):
    _inherit = 'purchase.order.line'
    
    last_cost = fields.Float(
        string='Last Cost', digits=dp.get_precision('Discount'), readonly=True
    )
    
    @api.onchange('product_id')
    def _compute_customer_code(self):
        if self.product_id:
            self.last_cost = self.product_id.standard_price