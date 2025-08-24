# -*- coding: utf-8 -*-
#################################################################################
# Author      : Acespritech Solutions Pvt. Ltd. (<www.acespritech.com>)
# Copyright(c): 2012-Present Acespritech Solutions Pvt. Ltd.
# All Rights Reserved.
#
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
#
#################################################################################

from odoo import models, fields, api, _


class PosOrder(models.Model):
    _inherit = "pos.order"

    @api.model
    def _order_fields(self, ui_order):
        order_fields = super(PosOrder, self)._order_fields(ui_order)
        order_fields['note'] = ui_order.get('order_note', False)
        return order_fields


class PosConfig(models.Model):
    _inherit = 'pos.config'

    enable_order_note = fields.Boolean('Order Note')
    enable_product_note = fields.Boolean('Product / Line Note')
    is_ordernote_receipt = fields.Boolean('Order Note on Receipt')
    is_productnote_receipt = fields.Boolean('Product / Line Note on Receipt')


class PosOrderLine(models.Model):
    _inherit = 'pos.order.line'

    line_note = fields.Char('Comment', size=512)
