# -*- coding: utf-8 -*-
#############################################################################
#
#    Labcit Inc.
#
#    Copyright (C) 2021-TODAY Labcit Inc. (<https://www.labcit.com>).
#    Author: Laboratorio en Tecnologias TIC @labcit(support@labcit.com)
#
#    You can modify it under the terms of the ALUF the Labcit Inc.
#
#############################################################################
from odoo import models, fields, api

class LcHrContract(models.Model):
    _name = 'lc.hr.contract'
    _description = 'Clauses of the employment contract'

    name = fields.Date(string="Date", required=True)
    template = fields.Text(string="Template", required=True)
    active = fields.Boolean(string="Active", required=True, default=True)

class LcHrInternalRegulations(models.Model):
    _name = 'lc.hr.internal.regulations'
    _description = 'Internal Regulations of working'

    name = fields.Date(string="Date", required=True)
    template = fields.Text(string="Template", required=True)
    active = fields.Boolean(string="Active", required=True, default=True)