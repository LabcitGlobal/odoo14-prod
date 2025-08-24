# -*- coding: utf-8 -*-

from odoo import models, fields, api


class LcImpuestoNit(models.Model):
    _name = 'lc.impuesto.nit'
    _description = 'Modelo para gestionar NIT'

    name = fields.Char('Contribuyente')    
    nit = fields.Char()
    domicilio_tributario = fields.Char()
    gran_actividad = fields.Char()
    actividad_principal = fields.Char()
    tipo_contribuyente = fields.Char()
    ubicacion = fields.Char()
    certificado = fields.Image(max_width=800)
    active = fields.Boolean('Activo', default=True)