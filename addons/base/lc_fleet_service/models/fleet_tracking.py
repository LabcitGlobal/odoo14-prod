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

class TrackingFleet(models.Model):
    _name = "lc.fleet.tracking"
    _description = "Tracking Fleet"

    service_id = fields.Many2one('lc.fleet.service', required=True, string="Service")
    date = fields.Datetime(string="Date", required=True, default=fields.Date.context_today)    
    name = fields.Text(string="Note", required=True)
    localization = fields.Many2one('res.country.state', required=True, string="Location")
    tracking_latitude = fields.Float(string="Latitude")
    tracking_longitude = fields.Float(string="Longitude")
    photo = fields.Image(string="Photo", max_width=800)
    file = fields.Binary(string="File")
    active = fields.Boolean('Active',default=True)