# -*- coding: utf-8 -*-

from odoo import models, fields, api, tools


class lcCommissionPosSubAgent(models.Model):
    _name = 'lccommission.possubagent'    
    _order = 'create_date desc' 

    name = fields.Many2one('pos.order','Orden', required=True)
    agent_id = fields.Many2one('lccommission.agent','Agente', required=True)
    note = fields.Text()    
    active = fields.Boolean('Activo', default=True)

class LcCommissionPosSubAgentView(models.Model):
    _name = 'lccommission.possubagent.view'
    _order = 'date_order desc' 
    _auto = False

    name = fields.Many2one('pos.order','Orden')
    agent_id = fields.Many2one('lccommission.agent','Agente')
    note = fields.Text()
    date_order = fields.Datetime('Fecha')
    user_id = fields.Many2one('res.users', 'Vendedor')
    partner_id = fields.Many2one('res.partner', 'Cliente')
    amount_total = fields.Float('Total')
    margin = fields.Float('Margen')
    payment = fields.Float('Pagado')

    def init(self):
        tools.drop_view_if_exists(self._cr, 'lccommission_possubagent_view')
        self._cr.execute("""
            create or replace view lccommission_possubagent_view as (
                select 
                	m.id, 
                	m.name, 
                	m.agent_id, 
                	m.note, 
                	o.date_order, 
                	o.user_id, 
                	o.partner_id, 
                    o.amount_total, 
                	o.margin, 
                	o.payment 
                from lccommission_possubagent m, pos_order o 
                where m.name=o.id
            )
        """)

