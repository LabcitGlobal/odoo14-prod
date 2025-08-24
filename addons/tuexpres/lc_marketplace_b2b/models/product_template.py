# -*- coding: utf-8 -*-

from odoo import models, fields, api

class product_template_b2b(models.Model):
     _inherit = 'product.template'
     
     marketplace_seller_id = fields.Many2one('res.partner')