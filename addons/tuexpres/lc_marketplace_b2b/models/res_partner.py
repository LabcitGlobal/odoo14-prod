# -*- coding: utf-8 -*-

from odoo import models, fields, api

class partner_b2b(models.Model):
     _inherit = 'res.partner'
     
     seller_commission = fields.Float(string="Seller Commission")     
     seller_investment = fields.Float(string="Seller Investment")