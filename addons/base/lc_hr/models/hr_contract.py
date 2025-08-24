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


class HrContract(models.Model):
    _inherit = 'hr.contract'
    _description = 'Contract Backup File'

    driver_license = fields.Selection([
        ('a','A'),
        ('b','B'),
        ('c','C')
        ], required=True, string="Driver License", default='c')
    vehicle_model = fields.Char(string="Model", required=True)
    vehicle_license_plate = fields.Char(string="License Plate", required=True)
    chassis = fields.Char(string="Chassis", required=True)
    color = fields.Char(string="Color", required=True)

    photo = fields.Image(string="Photo", max_width=800)
    file1 = fields.Binary(string="File 1")
    file2 = fields.Binary(string="File 2")
    file3 = fields.Binary(string="File 3")