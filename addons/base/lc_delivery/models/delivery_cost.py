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


class lcDeliveryCost(models.Model):
    _name = 'lc.delivery.cost'    

    name = fields.Many2one('res.partner','Partner')
    agency = fields.Many2one('res.partner','Agency')
    date = fields.Date('Date', required=True, index=True, default=fields.Date.context_today)
    pos_id = fields.Many2one('pos.order','Point Of Sale')
    sale_id = fields.Many2one('sale.order','Sales')
    number_of_boxes = fields.Float()
    mount = fields.Float()
    note = fields.Text('Note')
    photo = fields.Image('Photo', max_width=800)
    file = fields.Binary('File')
    note = fields.Text('Note')
    payment_type = fields.Selection([
        ('cash','Cash'),
        ('check','Check'),
        ('bank','Bank')
    ], 'Payment Type')
    payment_date = fields.Date('Payment Date')
    bank = fields.Many2one('res.bank', string="Bank")
    transaction_code = fields.Char(string="Transaction")
    state = fields.Selection([        
        ('pending', 'Pending'),                
        ('payment', 'Payment')
        ], 'State', default='pending', readonly=True,
        track_visibility="onchange",
        copy=False)
    company_id = fields.Many2one('res.company', string='Company', required=True, readonly=True, default=lambda self: self.env['res.company']._company_default_get('lc_delivery'))
    
    def _prepare_payment_values(self):
        return {
            'state': 'payment'            
        }

    def action_payment_delivery(self):
        if self.payment_type and self.payment_date:            
            self.write(self._prepare_payment_values())
        else:
            raise ValidationError(_('The following fields are required to set payment.\nComplete the data the detail payment tab.\n- Payment Type\n- Payment Date'))
        return True
    
    def _prepare_pending_values(self):
        return {
            'state': 'pending'            
        }

    def action_pending_delivery(self):        
        self.write(self._prepare_pending_values())        
        return True