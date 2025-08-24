# -*- coding: utf-8 -*-

from odoo import models, fields, api

class lc_pos_product_product(models.Model):
    _inherit = 'product.product'

    product_pos_enabled = fields.Boolean(string='Enable in POS', default=True)