# -*- coding: utf-8 -*-

from odoo import models, fields, api


class LcImpuestoVenta(models.Model):
    _name = 'lc.impuesto.venta'
    _description = 'Modelo para gestionar la factura de Venta'

    talonario_id = fields.Many2one('lc.impuesto.talonario', 'Talonario', required=True)
    fecha = fields.Date()
    numero = fields.Integer()
    cliente = fields.Many2one('res.partner', 'Cliente', required=True)
    name = fields.Char('Razon Social', required=True)
    nit = fields.Char()
    importe = fields.Float('Total')
    anulado = fields.Boolean('Anulado', default=False)
    foto = fields.Image(max_width=800)
    active = fields.Boolean('Activo', default=True) 