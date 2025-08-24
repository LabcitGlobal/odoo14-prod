# -*- coding: utf-8 -*-

from odoo import models, fields, api

class lc_pricelist_pos_config(models.Model):
    _inherit = 'pos.config'

    pricelist_group = fields.Boolean(string='Update Pricelist Group')

class lc_pricelist_product_template(models.Model):
    _inherit = 'product.template'

    product_template_price_group = fields.Boolean(string='Update Pricelist Group')