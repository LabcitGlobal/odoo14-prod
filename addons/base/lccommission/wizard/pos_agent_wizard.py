# -*- coding: utf-8 -*-
from odoo import models, fields


class LcPosAgentWizard(models.TransientModel):
    _name = 'lccommission.posagent.wizard'

    agent_id = fields.Many2one('lccommission.agent', string='Agente')
    posorder_ids = fields.Many2many('pos.order', string='Pedidos')

    def add_posorder_agent(self):
        posagentModel = self.env['lccommission.posagent']
        for wiz in self:
            for order in wiz.posorder_ids:
                posagentModel.create({
                    'agent_id': wiz.agent_id.id,
                    'name': order.id
                })
