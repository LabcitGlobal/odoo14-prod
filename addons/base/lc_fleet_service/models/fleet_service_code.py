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

# from typing_extensions import Required
from odoo import models, fields, api

class ServiceFleetCode(models.Model):
    _name = "lc.fleet.service.code"
    _description = "Service Fleet Code"
    

    def _prepare_enable_values(self):
        return {
            'state': 'enable',
        }
    
    def _prepare_disable_values(self):
        return {
            'state': 'disable'            
        }
    
    def action_enable_fleet_code(self):
        self.write(self._prepare_enable_values())
        return True

    def action_disable_fleet_code(self):
        self.write(self._prepare_disable_values())
        return True

    name = fields.Char(string="Code", copy=False, default="New", readonly=True, required=True)
    note = fields.Char(string="Note")
    user_id = fields.Many2one('res.users', readonly=True, string="User", default=lambda self: self.env.user)
    state = fields.Selection([
        ('enable','Enable'),
        ('disable','Disable'),
    ], string="State", readonly=True, required=True, default='enable')

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('fleet.service.code') or 'New'
        
        result = super(ServiceFleetCode, self).create(vals)
        return result