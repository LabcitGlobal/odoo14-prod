# -*- coding: utf-8 -*-

from odoo import models, fields, api

class marketplace_dashboard(models.Model):
    _name = "marketplace.b2b"
    _description = "Marketplace B2B"

    name = fields.Char(string="Name", translate=True)