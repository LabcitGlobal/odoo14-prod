# -*- coding: utf-8 -*-

from odoo import models, fields, api

class lcsupport_service(models.Model):
    _inherit = 'lcsupport.service'

    trackingservice_ids = fields.One2many(
        'lcsupport.tracking', 'service_id', 'Seguimiento'
    )

class lcsupport_tracking(models.Model):
    _name = 'lcsupport.tracking'
    _description = 'Tracking de Servicio'
    _order = "create_date desc"
        
    service_id = fields.Many2one('lcsupport.service','Seguimiento',required=True)
    issue_description = fields.Text(required=True)