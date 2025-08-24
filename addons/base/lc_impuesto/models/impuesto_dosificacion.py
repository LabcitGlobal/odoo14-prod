# -*- coding: utf-8 -*-

from odoo import models, fields, api


class LcImpuestoDosificacion(models.Model):
    _name = 'lc.impuesto.dosificacion'
    _description = 'Modelo para gestionar la dosificacion'
    
    nit_id = fields.Many2one('lc.impuesto.nit', 'Nit', required=True)
    fecha_emision = fields.Date()
    limite_emision = fields.Date()    
    name = fields.Char('Autorizacion')
    cantidad = fields.Integer()
    desde = fields.Integer()
    hasta = fields.Integer()    
    talonarios = fields.Integer()
    observaciones = fields.Char()        
    dosificacion = fields.Image(max_width=800)
    active = fields.Boolean('Activo', default=True) 