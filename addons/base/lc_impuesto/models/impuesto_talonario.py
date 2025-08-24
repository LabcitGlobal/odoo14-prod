# -*- coding: utf-8 -*-

from odoo import models, fields, api


class LcImpuestoTalonario(models.Model):
    _name = 'lc.impuesto.talonario'
    _description = 'Modelo para gestionar el talonario'

    dosificacion_id = fields.Many2one('lc.impuesto.dosificacion', String='Dosificacion', required=True)
    name = fields.Char('Talonario')
    desde = fields.Integer()
    hasta = fields.Integer()
    fecha_activacion = fields.Date()    
    habilitado = fields.Boolean(default=False)
    active = fields.Boolean('Activo', default=True)