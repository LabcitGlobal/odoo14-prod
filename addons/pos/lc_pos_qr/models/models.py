# -*- coding: utf-8 -*-

from odoo import models, fields, api

class PosQrCode(models.Model):
    _name = 'lc.pos.qr'
    _description = 'Payment in POS by QR'
    
    def _prepare_enable_values(self):
        return {
            'state': 'enable',
        }
    
    def _prepare_disable_values(self):
        return {
            'state': 'disable'            
        }
    
    def action_enable_qr_code(self):
        self.write(self._prepare_enable_values())
        return True

    def action_disable_qr_code(self):
        self.write(self._prepare_disable_values())
        return True

    name = fields.Char(required=True, string="Account name")
    bank_id = fields.Many2one('res.bank',required=True, string="Bank")
    number_account= fields.Char(required=True, string="Account number")
    currency_id = fields.Many2one('res.currency', required=True, string="Currency")
    note = fields.Char(string="Note")
    user_id = fields.Many2one('res.users', readonly=True, string="User", default=lambda self: self.env.user)
    date = fields.Date(string='Date', default=fields.Date.context_today)
    qr_code_image = fields.Binary(string='Qr Image')
    state = fields.Selection([
        ('enable','Enable'),
        ('disable','Disable'),
    ], string="State", readonly=True, required=True, default='enable')
