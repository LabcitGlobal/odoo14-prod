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

# from typing_extensions import Required
from odoo import models, fields

class RemissionFleet(models.Model):
    _name = "lc.fleet.remission"
    _description = "Remission Fleet"

    name = fields.Many2one('lc.fleet.service', required=True, string="Service")
    date_today = fields.Date(string="Date", required=True, default=fields.Date.context_today)    
    remission_document_ids = fields.One2many('lc.fleet.remission.document','remission_id', required=True, string="Documents")
    state = fields.Boolean(default=False, string="State")


class DocumentTypeFleet(models.Model):
    _name = "lc.fleet.remission.document.type"
    _description = "Remission Document Type"

    name = fields.Char(string="Name", required=True)


class DocumentRemissionFleet(models.Model):
    _name = "lc.fleet.remission.document"
    _description = "Remission Document"

    remission_id = fields.Many2one('lc.fleet.remission', required=True, string="Remission")
    document_type_id = fields.Many2one('lc.fleet.remission.document.type', required=True, string="Document")
    code = fields.Char(required=True, string="Code")
    quantity = fields.Integer(required=True, default="1", string="Quantity")
    file1 = fields.Binary(string="File 1")
    file2 = fields.Binary(string="File 2")
    file3 = fields.Binary(string="File 3")
    type = fields.Selection([('original','Original'),('copia','Copy'),('photocopy','Photocopy')], required=True, string="Type")
    active = fields.Boolean('Active', default=True)

