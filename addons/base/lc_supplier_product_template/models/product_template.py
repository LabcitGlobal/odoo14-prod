# -*- coding: utf-8 -*-

from odoo import models, fields, api

class lc_product_template(models.Model):
     _inherit = 'product.template'
     
     supplier_id = fields.Many2one('res.partner', groups="lc_hide_margin_pos.sec_lc_hide_margin_pos")
     supplier_commission_type_id = fields.Many2one('lc.type.supplier.commission',string='Type of Supplier Commission', groups="lc_hide_margin_pos.sec_lc_hide_margin_pos")
     supplier_commission = fields.Float(string="Supplier Commission", groups="lc_hide_margin_pos.sec_lc_hide_margin_pos")

     supplier_purchase_type_id = fields.Many2one('lc.type.supplier.purchase', string='Type of Supplier Purchase', groups="lc_hide_margin_pos.sec_lc_hide_margin_pos")
     supplier_cost = fields.Float(string="Supplier Cost", groups="lc_hide_margin_pos.sec_lc_hide_margin_pos")
     supplier_selling_price = fields.Float(string="Supplier Selling Price", groups="lc_hide_margin_pos.sec_lc_hide_margin_pos")    
     supplier_real_commission = fields.Float(string="Supplier Real Commission", compute='_compute_supplier_real_commission', groups="lc_hide_margin_pos.sec_lc_hide_margin_pos")
     supplier_new_sale_price = fields.Float(string="Supplier New Sale Price", compute='_compute_new_sale_price', groups="lc_hide_margin_pos.sec_lc_hide_margin_pos")

     @api.depends("supplier_selling_price", "supplier_cost", "supplier_commission")
     def _compute_supplier_real_commission(self):
        for record in self:
            record.supplier_real_commission = (record.supplier_selling_price - record.supplier_cost) * record.supplier_commission   
     
     @api.depends("supplier_selling_price", "supplier_cost", "supplier_commission")
     def _compute_new_sale_price(self):
        for record in self:
            record.supplier_new_sale_price = record.supplier_selling_price - ((record.supplier_selling_price - record.supplier_cost) * record.supplier_commission)
     

class TypeSupplierCommission(models.Model):
    _name = "lc.type.supplier.commission"

    name = fields.Char(string="Type", required=True)

class TypeSupplierPurchase(models.Model):
    _name = "lc.type.supplier.purchase"

    name = fields.Char(string="Type", required=True)
     