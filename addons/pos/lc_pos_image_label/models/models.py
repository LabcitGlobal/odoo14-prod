# -*- coding: utf-8 -*-

from odoo import models, fields, api
from mako.runtime import _inherit_from

class lc_pos_image_label(models.Model):
     _inherit = 'product.product'

     label1 = fields.Char(string='Label 1')
     label2 = fields.Char(string='Label 2')
     top = fields.Selection([('1', 'Liquidación'), ('2', 'Promoción'), ('3', 'Paquete'), ('4', 'Unidad')], 'top', default='')