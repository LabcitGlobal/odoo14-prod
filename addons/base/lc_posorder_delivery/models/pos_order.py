# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models

class PosOrderShipping(models.Model):
    _inherit = 'pos.order'

    shipping_company = fields.Many2one('res.partner', 'Transportadora')
    shipping_partner = fields.Many2one('res.partner', 'Responsable')
    destiny = fields.Many2one('res.country.municipalities', 'Destino')
    box_quantity = fields.Float('Cant. Cajas')
    passage = fields.Selection([
        ('to_pay','Por Pagar'),
        ('paid_out','Pagado')
    ], 'Pasaje', default="to_pay")
    shipping_cost = fields.Float('Costo de Envío')
    shipping_payment = fields.Float('Pago de Envío')
    shipping_note = fields.Text('Nota')
    deposit_file = fields.Binary(string="Deposito")
    office_guide = fields.Binary(string="Guia de despacho")
    pos_file = fields.Binary(string="Respaldo")
    pos_photo1 = fields.Image('Respaldo 1', max_width=800)
    pos_photo2 = fields.Image('Respaldo 2', max_width=800)
    pos_photo3 = fields.Image('Respaldo 3', max_width=800)
    shipping_date = fields.Date(string="Fecha de Envio", index=True)
    deposit_account = fields.Many2one('hr.employee', 'Cuenta')
    bank_account = fields.Many2one('res.bank', string="Banco")

