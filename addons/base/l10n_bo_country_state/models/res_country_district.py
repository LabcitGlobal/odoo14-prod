# -*- coding: utf-8 -*-

from odoo import models, fields, api

class District(models.Model):
    _description = 'District'
    _name = 'res.country.district'
    _order = 'municipality_id'

    municipality_id = fields.Many2one('res.country.municipalities', string="Municipality", required=True)
    name = fields.Char(string="District name", required=True)
    code = fields.Char(string="District Code", required=True)
    active = fields.Boolean(default=True)