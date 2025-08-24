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
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class VehicleInventory(models.Model):
    _name = "lc.vehicle.parts.inventory"
    _description = "Vehicle parts inventory information"
    
    name = fields.Many2one('fleet.vehicle', string="Name", required=True)
    date_today = fields.Date(string="Date", required=True, index=True, default=fields.Date.context_today)
    note = fields.Text(string="Note")
    file = fields.Binary(string="File (Pdf)")
    part_list_ids = fields.One2many('lc.vehicle.parts.inventory.details', 'part_inventory_id', string="Part List", required=True)
   
class VehicleInventoryDetail(models.Model):
    _name = "lc.vehicle.parts.inventory.details"
    _description = "Vehicle parts inventory details information"

    part_inventory_id = fields.Many2one('lc.vehicle.parts.inventory', string="Vehicle Inventory", required=True)
    part_id = fields.Many2one('lc.vehicle.parts.list', string="Part List", required=True, domain=[('parent_id','!=',False)])
    quantity_parts = fields.Float(string="Quantity Parts", required=True, default=1)
    part_note = fields.Char(string="Note")


class VehiclePart(models.Model):
    _name = "lc.vehicle.parts.list"
    _description = "Vehicle Parts List"

    _parent_store = True
    _parent_name = 'parent_id'

    name = fields.Char(string="Part Name", required=True)
    active = fields.Boolean('Active', default=True)
    
    parent_id = fields.Many2one('lc.vehicle.parts.list',string="Parent Part Category", ondelete='restrict', index=True)
    parent_path = fields.Char(index=True)

    @api.constrains('parent_id')
    def _check_hierarchy(self):
        if not self._check_recursion():
            raise models.ValidationError('Error: You cannot create recursive categories.')