# Copyright (C) Softhealer Technologies.
# Part of Softhealer Technologies.

from odoo import models, fields


class PosConfig(models.Model):
    _inherit = 'pos.config'

    enable_numpad = fields.Boolean(string='Hide/Show Numpad')
