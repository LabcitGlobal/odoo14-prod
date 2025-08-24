# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Municipalities(models.Model):
    _description = 'Municipalities'
    _name = 'res.country.municipalities'
    _order = 'province_id'

    province_id = fields.Many2one('res.country.province', string="Province", required=True)
    name = fields.Char(string="Municipality Name", required=True)
    code = fields.Char(string="Municipality Code", required=True)
    active = fields.Boolean(default=True)