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

from odoo.exceptions import ValidationError
from datetime import time, timedelta
from odoo import models, fields, api, _

class ContainerControl(models.Model):
    _name = "lc.container.control"
    _description = "Container Control"
    
    def get_container_control_file_count(self):
        count = self.env['lc.container.file'].search_count([('container_id','=',self.id)])
        self.container_control_file = count

    def open_container_control_file(self):
        return {
            'name': 'Container Documents Files',
            'domain': [('container_id','=',self.id)],            
            'res_model': 'lc.container.file',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }
    
    def _prepare_draft_values(self):
        return {
            'state': 'draft'            
        }
    
    def _prepare_confirmation_values(self):
        return {
            'state': 'service'
        }
    
    def _prepare_finished_values(self):
        return {
            'state': 'finished',
            'return_date': fields.Datetime.now()
        }
       
    def action_confirm_container_control(self):
        if self.vehicle_ids:
            self.write(self._prepare_confirmation_values())
        else:
            raise ValidationError(_('The following fields are required to services case.\nComplete the data.\n- Vehicle ID'))
        return True
        
    def action_draft_container_control(self):
        self.write(self._prepare_draft_values())
        return True
    
    def action_finished_container_control(self):
        if self.date_in_port:
            self.write(self._prepare_finished_values())
        else:
            raise ValidationError(_('The following fields are required to finished case.\nComplete the data.\n- Date in port'))
        return True

    name = fields.Char(string="Code", copy=False, default="New", readonly=True, required=True)
    date_today = fields.Date(string="Date", required=True, index=True, default=fields.Date.context_today)
    customer_id = fields.Many2one('res.partner',string="Customer")
    date_of_assignment = fields.Date(string="Date of Assignment", required=True, help="Container arrival date")
    expiration_date = fields.Date(string="Expiration Date", help="Container return deadline")
    expires_in = fields.Integer(string="Expires in", compute='_compute_date', inverse='_inverse_date', help="Days on which the container delivery time ends")
    drop_off_location = fields.Many2one('lc.fleet.localization', string="Drop off location")
    notes = fields.Text(string="Detail")
    return_date = fields.Date(string="Return Date")
    return_note = fields.Text(string="Return Note")
    user_id = fields.Many2one('res.users', string="Salesperson", default=lambda self: self.env.user)
    vehicle_ids = fields.One2many('lc.container.vehicle', 'container_id', required=True, string="Vehicles")
    route_ids = fields.One2many('lc.container.route','container_id', required=True, string="Route")    
    container_file_ids = fields.One2many('lc.container.file','container_id', required=True, string="Container File")    
    state = fields.Selection([
        ('draft','Quotation'),
        ('service','Service Order'),
        ('finished','Finished')
        ], required=True, string="Status", readonly=True, copy=False, index=True, default='draft')
    container_control_file = fields.Integer(string="Files", compute='get_container_control_file_count')
    active = fields.Boolean('Active', default=True)

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('container.control.code') or 'New'
        
        result = super(ContainerControl, self).create(vals)
        return result

    @api.depends('expiration_date')
    def _compute_date(self):
        today = self.date_today
        for control in self:
            if control.expiration_date:
                delta = self.expiration_date - today
                control.expires_in = delta.days
            else:
                control.expires_in = 0
    
    def _inverse_date(self):
        for control in self.filtered('expires_in'):
            control.expiration_date = control.date_today + timedelta(days=control.expires_in)



class ContainerRoute(models.Model):
    _name = "lc.container.route"
    _description = "Container Route"

    container_id = fields.Many2one('lc.container.control', required=True, string="Container")
    source = fields.Many2one('lc.fleet.localization', required=True, string="Source")
    destination = fields.Many2one('lc.fleet.localization', required=True, string="Destination")
    active = fields.Boolean('Active', default=True)

class ContainerVehicle(models.Model):
    _name = "lc.container.vehicle"
    _description = "Container Drivers and Vehicles"

    container_id = fields.Many2one('lc.container.control', required=True, string="Container")
    vehicle_id = fields.Many2one('fleet.vehicle', required=True, string="Vehicle")
    driver_id = fields.Many2one('res.partner', required=True, string="Driver")