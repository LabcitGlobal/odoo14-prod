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

class DriverExpensesFleet(models.Model):
    _name = "lc.fleet.driver.expenses"
    _description = "Driver Expenses Fleet"

    service_id = fields.Many2one('lc.fleet.service', required=True, string="Service")
    date = fields.Datetime(index=True, default=fields.Date.context_today, string="Date and Time")
    category_expenses_id = fields.Many2one('lc.fleet.category.expenses', required=True, string="Category")
    name = fields.Text(string="Detail")
    amount = fields.Float(required=True, string="Amount")
    currency_id = fields.Many2one('res.currency','Currency', default=lambda self: self.env.company.currency_id.id)
    photo = fields.Image(string="Photo", max_width=800)
    file = fields.Binary(string="File")
    active = fields.Boolean('Active', default=True)

class CategoryExpensesFleet(models.Model):
    _name = "lc.fleet.category.expenses"
    _description = "Category Expenses Driver"

    name = fields.Char(required=True, string="Category")
    active = fields.Boolean('Active', default=True)