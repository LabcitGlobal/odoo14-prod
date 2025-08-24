# -*- coding: utf-8 -*-

from odoo import models, fields, api, tools

class LcCreditPartnerView(models.Model):
    _name = "lc.credit.partner.view"    
    _auto = False
    
    partner_id = fields.Many2one('res.partner', 'Cliente')
    name = fields.Char('Cliente')
    total = fields.Float('Total')
    payment = fields.Float('Pagado')
    pending = fields.Float('Pendiente')    

    def init(self):        
        tools.drop_view_if_exists(self._cr, 'lc_credit_partner_view')        
        self._cr.execute("""        
            create or replace view lc_credit_partner_view as (
                select 
                	o.partner_id as id,
                    o.partner_id,
                	r.name, 
                	round(sum(o.amount_total),2) as total, 
                	round(sum(coalesce(o.payment,0))::numeric,2) as payment, 
                	round(sum(o.amount_total)-sum(coalesce(o.payment,0))::numeric,2) as pending 
                from pos_order o, res_partner r
                where o.partner_id = r.id and o.partner_id in(
                	select distinct partner_id from pos_order where amount_total!=coalesce(payment,0) and amount_total-coalesce(payment,0)>1
                ) 
                group by o.partner_id, r.name
                having round(sum(o.amount_total)-sum(coalesce(o.payment,0))::numeric,2) > 1 or round(sum(o.amount_total)-sum(coalesce(o.payment,0))::numeric,2) < -1
            )""")