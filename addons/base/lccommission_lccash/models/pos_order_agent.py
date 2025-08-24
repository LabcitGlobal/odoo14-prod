# -*- coding: utf-8 -*-

from odoo import models, fields, api

class lc_commission_pos_order(models.Model):     
     _inherit = 'pos.order'
          
     delivery_id = fields.Many2one('lccommission.agent','Chofer')
     packer_id = fields.Many2one('lccommission.agent','Alistador')