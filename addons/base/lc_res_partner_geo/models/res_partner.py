# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _

class ResPartner(models.Model):
    _inherit = "res.partner"

    partner_latitude = fields.Float('Geo Latitude', digits=(10, 7), default="-16.492671")
    partner_longitude = fields.Float('Geo Longitude', digits=(10, 7), default="-68.191087")
