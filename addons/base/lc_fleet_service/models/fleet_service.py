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
from odoo.exceptions import ValidationError
from num2words import num2words
from odoo import models, fields, api, _

class ServiceFleet(models.Model):
    _name = "lc.fleet.service"
    _description = "Service Fleet"

    _parent_store = True
    _parent_name = "parent_id"
    
    name = fields.Many2one('lc.fleet.service.code',string="Code")
    date_today = fields.Date(string="Date", required=True, index=True, default=fields.Date.context_today)
    customer_id = fields.Many2one('res.partner',string="Customer")
    notes = fields.Text(string="Detail")
    amount = fields.Monetary(string="Amount")
    currency_id = fields.Many2one('res.currency','Currency', default=lambda self: self.env['res.currency'].search([('name', '=', 'USD' )]).id)
    debit_date_today = fields.Date(string="Date", required=True, default=fields.Date.context_today)
    invoice_number = fields.Char(string="Invoice Number")
    fleet_remission_count = fields.Integer(string="Remission", compute='get_remission_count')    
    driver_expenses_total = fields.Float(string="Expenses", compute='get_driver_expenses_total')    
    fleet_tracking_count = fields.Integer(string="Tracking", compute='get_tracking_count')        
    user_id = fields.Many2one('res.users', string="Salesperson", default=lambda self: self.env.user)
    debit_date = fields.Date(string="Date")
    vehicle_ids = fields.One2many('lc.fleet.service.vehicle', 'service_id', required=True, string="Vehicles")
    route_ids = fields.One2many('lc.fleet.route','service_id', required=True, string="Route")    
    payment = fields.Float(string="Payment")
    state = fields.Selection([
        ('draft','Quotation'),
        ('service','Service Order'),
        ('cancel','Cancelled'),
        ('payed','Payed')
        ], required=True, string="Status", readonly=True, copy=False, index=True, default='draft')
    expenses_ids = fields.One2many('lc.fleet.driver.expenses','service_id',string="Expenses")
    
    parent_id = fields.Many2one('lc.fleet.service', string="Parent Service", ondelete='restrict', index=True, domain=[('apportionment','=',False)])
    apportionment = fields.Boolean(string="Apportionment", default=False, readonly=True, copy=False)
    proration_percentage = fields.Float(string="Proration Percentage", default=00.5)
    parent_path = fields.Char(index=True)
    margin = fields.Float(string="Margin", compute='get_margin_total')
    active = fields.Boolean('Active', default=True)


    @api.constrains('parent_id')
    def _check_hierarchy(self):
        if not self._check_recursion():
            raise models.ValidationError('Error! You cannot create recursive categories.')

    def get_code_number(self):        
        service = self.env['lc.fleet.service'].search([('id','=',self.id)])        
        sequence = self.env['ir.sequence'].search([('code','=','fleet.service.code')])        
        return service.name.name[len(sequence.prefix):len(service.name.name)]

    def amount_to_tex(self,amount):
        return num2words(amount,lang='es')
    
    def get_remission_count(self):
        count = self.env['lc.fleet.remission'].search_count([('name','=',self.id)])
        self.fleet_remission_count = count

    def get_tracking_count(self):
        count = self.env['lc.fleet.tracking'].search_count([('service_id','=',self.id)])
        self.fleet_tracking_count = count
    
    def get_driver_expenses_total(self):
        reg = self.env['lc.fleet.driver.expenses'].search([('service_id','=',self.id)])
        total = 0
        for line in reg:
            total = total + line.currency_id._convert(line.amount, self.env.company.currency_id, self.env.company, line.date)
        self.driver_expenses_total = total

    def get_margin_total(self):
        amount = self.currency_id._convert(self.amount, self.env.company.currency_id, self.env.company, self.date_today)
        self.margin = amount - self.driver_expenses_total

    def open_fleet_remission(self):
        return {
            'name': 'Remission',
            'domain': [('name','=',self.id)],            
            'res_model': 'lc.fleet.remission',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }
    
    def open_driver_expenses(self):
        return {
            'name': 'Expenses',
            'domain': [('service_id','=',self.id)],            
            'res_model': 'lc.fleet.driver.expenses',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }

    def open_tracking(self):
        return {
            'name': 'Tracking',
            'domain': [('service_id','=',self.id)],            
            'res_model': 'lc.fleet.tracking',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }        
    
    def _prepare_confirmation_values(self):
        return {
            'state': 'service',
            'debit_date': fields.Datetime.now()
        }
    
    def _prepare_cancel_values(self):
        return {
            'state': 'cancel'            
        }
    
    def _prepare_draft_values(self):
        return {
            'state': 'draft'            
        }
    
    def _prepare_payed_values(self):
        return {
            'state': 'payed'            
        }
    
    def _prepare_apportionment_values(self):
        return {
            'apportionment': 'True'            
        }

    def _copy_service_charges(self):        
        reg = self.env['lc.fleet.driver.expenses'].search([('service_id','=',self.parent_id.id)])
        for line in reg:
            values = {
                'service_id': self.id,
                'date': line.date,
                'category_expenses_id': line.category_expenses_id.id,
                'name': line.name,
                'amount': line.amount*(self.proration_percentage),
                'currency_id': line.currency_id.id
            }
            self.env['lc.fleet.driver.expenses'].create(values)
            line.update({
                'amount': line.amount*(self.proration_percentage)
            })
        
        self.update({
            'apportionment': True
        })
        self.parent_id.update({
            'apportionment': True
        })


    def action_confirm_fleet_service(self):
        if self.customer_id and self.notes and self.amount and self.currency_id:
            if self.name:
                self.name.update({'state': 'disable'})
            self.write(self._prepare_confirmation_values())
        else:
            raise ValidationError(_('The following fields are required to generate a debit note.\nComplete the data in the debit note tab.\n- Code\n- Customer\n- Note\n- Amount\n- Currency'))
        return True
    
    def action_cancel_fleet_service(self):
        self.write(self._prepare_cancel_values())
        return True
    
    def action_draft_fleet_service(self):
        self.write(self._prepare_draft_values())
        return True
    
    def action_payed_fleet_service(self):
        if self.payment == self.amount:
            self.write(self._prepare_payed_values())
        else:
            raise ValidationError(_('The amount of the service is different from the amount paid'))
        return True

    def action_prorate_now(self):
        if self.parent_id and self.proration_percentage:            
            if self.apportionment==False:
                self._copy_service_charges()
                self.write(self._prepare_apportionment_values())
            else:
                raise ValidationError(_('This service has already been prorated for your expenses.'))
        else:
            raise ValidationError(_('The following fields are required to generate the apportionment of this service.\nComplete the data in the Apportionment note tab.\n- Parent Service\n- Proration Percentage'))
        return True
    

class LocalizationFleet(models.Model):
    _name = "lc.fleet.localization"

    name = fields.Char(string="Location", required=True)


class RouteFleet(models.Model):
    _name = "lc.fleet.route"
    _description = "Route Fleet"

    service_id = fields.Many2one('lc.fleet.service', required=True, string="Service")
    source = fields.Many2one('lc.fleet.localization', required=True, string="Source")
    destination = fields.Many2one('lc.fleet.localization', required=True, string="Destination")
    active = fields.Boolean('Active', default=True)

class ServiceVehicle(models.Model):
    _name = "lc.fleet.service.vehicle"
    _description = "Service Drivers and Vehicles"

    service_id = fields.Many2one('lc.fleet.service', required=True, string="Service")
    vehicle_id = fields.Many2one('fleet.vehicle', required=True, string="Vehicle")
    driver_id = fields.Many2one('res.partner', required=True, string="Driver")

