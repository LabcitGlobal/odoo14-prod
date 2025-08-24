# -*- coding: utf-8 -*-

from odoo import models, fields, api


class LcImpuestoCompra(models.Model):
    _name = 'lc.impuesto.compra'
    _description = 'Modelo para gestionar la factura de Compra'

    nit_id = fields.Many2one('lc.impuesto.nit', 'Nit', required=True)    
    fecha = fields.Date()
    numero = fields.Integer()
    proveedor = fields.Many2one('res.partner', 'Proveedor', required=True)
    name = fields.Char('Nit Proveedor')
    razon_social = fields.Char()    
    total = fields.Float()   
    observacion = fields.Char() 
    foto = fields.Image(max_width=800)    
    active = fields.Boolean('Activo', default=True)