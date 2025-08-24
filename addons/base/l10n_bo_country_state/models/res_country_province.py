# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Province(models.Model):
    _description = 'Province'
    _name = 'res.country.province'
    _order = 'department_id'

    department_id = fields.Many2one('res.country.state', string="Departments", required=True)
    name = fields.Char(string="Province name", required=True)
    code = fields.Char(string="Province Code", required=True)
    active = fields.Boolean(default=True)