# -*- coding: utf-8 -*-

from odoo import models, fields, api


class lcCommissionType(models.Model):
    _name = 'lccommission.type'    

    name = fields.Char()
    active = fields.Boolean('Activo', default=True)

class lcCommissionTypeAgent(models.Model):
    _name = 'lccommission.type.agent'    

    name = fields.Char()
    active = fields.Boolean('Activo', default=True)

class lcCommissionAgent(models.Model):
    _name = 'lccommission.agent'

    name = fields.Many2one('res.users','Usuario', required=True)
    type_id = fields.Many2one('lccommission.type','Tipo de Comision', required=True)
    t_agent_id = fields.Many2one('lccommission.type.agent', 'Tipo de Agente', required=True)
    value_fixed = fields.Float('Fijo')
    value_commission = fields.Float('Comision')
    active = fields.Boolean('Activo', default=True)
