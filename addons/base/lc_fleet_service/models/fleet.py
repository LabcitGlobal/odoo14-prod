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


class FleetVehicle(models.Model):
    _inherit = 'fleet.vehicle'

    fleet_check_availability = fields.Boolean(default=True, copy=False)