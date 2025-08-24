# -*- coding: utf-8 -*-

from odoo import models, fields, api, tools

class LcCreditPosView(models.Model):
    _name = "lc.credit.pos.view"
    _order = "id desc"
    _auto = False

    name = fields.Char()
    pos_reference = fields.Char()
    client = fields.Char('Cliente')
    date_order = fields.Datetime('Fecha de Pedido')
    seller = fields.Char('Vendedor')
    amount_total = fields.Float('Total')
    payment = fields.Float('Pagado')
    state = fields.Char('Estado')

    def init(self):        
        tools.drop_view_if_exists(self._cr, 'lc_credit_pos_view')        
        self._cr.execute("""        
            CREATE or REPLACE VIEW lc_credit_pos_view AS (
                SELECT 
                o.id, 
                o.name, 
                o.pos_reference, 
                p.name as client, 
                o.date_order, 
                e.name as seller, 
                ROUND(COALESCE(o.amount_total,0),2) AS amount_total, 
                COALESCE(o.payment,0) AS payment, 
                o.state 
                FROM pos_order o, res_partner p, res_users u, res_partner e 
                WHERE o.partner_id=p.id AND o.user_id=u.id AND u.partner_id=e.id AND TRUNC(COALESCE(amount_total,0)) != TRUNC(COALESCE(o.payment,0))                
            )""")