# -*- coding: utf-8 -*-

from odoo import models, fields, api

class AwardsPartner(models.Model):
    _name = "lc.partner.awards"

    name = fields.Many2one('res.partner', 'Partner')
    pos_order_id = fields.Many2one('pos.order')
    note = fields.Text()