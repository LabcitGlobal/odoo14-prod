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

from odoo import models, fields,_

class ContainerFile(models.Model):
    _name = "lc.container.file"
    _description = "Container Documents Files"

    container_id = fields.Many2one('lc.container.control', string="Container Control", required=True)
    date = fields.Date(string="Date", required=True, default=fields.Date.context_today)
    file_category_id = fields.Many2one('lc.file.category', string="File Category", required=True)
    name = fields.Char(string="Code/Number")
    quantity = fields.Integer(required=True, default="1", string="Quantity")
    photo = fields.Image(string="Photo", max_width=800)    
    file1 = fields.Binary(string="File 1")
    file2 = fields.Binary(string="File 2")
    file3 = fields.Binary(string="File 3")
    type = fields.Selection([('original','Original'),('copia','Copy'),('photocopy','Photocopy')], required=True, string="Type")
    active = fields.Boolean('Active', default=True)


class FileCategory(models.Model):
    _name = "lc.file.category"
    _description = "File Category"

    name = fields.Char(string="Name", required=True)
    active = fields.Boolean('Active', default=True)