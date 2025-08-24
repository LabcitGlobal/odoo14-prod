# -*- coding: utf-8 -*-

from odoo import models, fields, api


class lcPosDisableOptions(models.Model):
    _inherit = 'pos.config'

    disable_discount = fields.Boolean('Enable/Disable Discount Button', default=True)
    disable_price = fields.Boolean('Enable/Disable Price Button', default=True)
    disable_payment = fields.Boolean('Enable/Disable Payment Button', default=True)
    # disable_quantity = fields.Boolean('Enable/Disable Quantity Button', default=True)
    # disable_payment = fields.Boolean('Enable/Disable Payment Button', default=True)
    # disable_customer = fields.Boolean('Enable/Disable Customer Button', default=True)
    