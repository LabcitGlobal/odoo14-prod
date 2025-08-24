# -*- coding: utf-8 -*-

from odoo import models, fields, api, tools


class LcPartnerPosOrder(models.Model):
    _name = "lc.partner.pos.view"
    _auto = False
    _order = 'margin desc'

    name = fields.Char('Cliente')
    orders = fields.Float('Orders')
    total = fields.Float('Total')
    margin = fields.Float('Margin')

    def init(self):        
        tools.drop_view_if_exists(self._cr, 'lc_partner_pos_view')        
        self._cr.execute("""        
            CREATE or REPLACE VIEW lc_partner_pos_view AS (
            SELECT 
                p.id, 
                p.name, 
                COUNT(*) AS orders, 
                ROUND(SUM(o.amount_total),2) AS total, 
                ROUND(SUM(o.margin),2) AS margin 
            FROM pos_order o, res_partner p 
            WHERE o.partner_id=p.id 
            GROUP BY p.id, p.name
            )""")