# -*- coding: utf-8 -*-

from odoo import models, fields, api, tools


class lcCommissionPosFile(models.Model):
    _name = 'lccommission.posfile'
    _order = 'write_date desc'    

    name = fields.Selection([('order','Boleta'),('shop','Tienda')], 'Tipo', default="order")
    pos_id = fields.Many2one('pos.order','Orden', required=True)
    pos_photo1 = fields.Image('Foto de la Boleta 1', max_width=800)
    pos_photo2 = fields.Image('Foto de la Boleta 2', max_width=800)
    pos_photo3 = fields.Image('Foto de la Boleta 3', max_width=800)
    note = fields.Text()
    active = fields.Boolean('Activo', default=True)

class LcCommissionPosFileView(models.Model):
    _name = 'lccommission.posfile.view'
    _order = 'id desc' 
    _auto = False

    name = fields.Text('Tipo')
    pos_id = fields.Many2one('pos.order','Orden')    
    note = fields.Text()
    date_order = fields.Datetime('Fecha')
    user_id = fields.Many2one('res.users', 'Vendedor')
    amount_total = fields.Float('Total')
    payment = fields.Float('Pagado')

    def init(self):
        tools.drop_view_if_exists(self._cr, 'lccommission_posfile_view')
        self._cr.execute("""
            create or replace view lccommission_posfile_view as (
                select 
                	m.id, 
                	m.name,
                    m.pos_id, 
                	m.note, 
                	o.date_order, 
                	o.user_id, 
                	o.amount_total,                 	
                	o.payment 
                from lccommission_posfile m, pos_order o 
                where m.pos_id=o.id
            )
        """)