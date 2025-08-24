# -*- coding: utf-8 -*-
#############################################################################
#
#    Labcit Inc.
#
#    Copyright (C) 2021-TODAY Labcit Inc. (<https://www.labcit.com>).
#    Author: Laboratorio en Tecnologias Tic @labcit(support@labcit.com)
#
#    You can modify it under the terms of the ALUF the Labcit Inc.
#
#############################################################################

from odoo import models, fields


class FleetBankAccount(models.Model):
    _name = 'lc.fleet.bank.account'
    _describe = 'Fleet Service Bank Account'

    name = fields.Many2one('res.bank',required=True, string="Bank")
    name_account = fields.Char(required=True, string="Account name")
    number_account= fields.Char(required=True, string="Account number")
    currency_id = fields.Many2one('res.currency', required=True, string="Currency")
    active = fields.Boolean('Active', default=True)