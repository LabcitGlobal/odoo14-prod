# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime

class LcCashChange(models.Model):
    _name = 'lccash.change'
    _description = 'Modelo para gestion de Cambios'
    _order = 'id desc'

    def _get_employee_id(self):
        employee_rec = self.env['hr.employee'].search([('user_id', '=', self.env.uid)], limit=1)
        return employee_rec.id

    name = fields.Many2one('hr.employee','Responsable',help='Quien dejo el Cambio', default=_get_employee_id)
    mount = fields.Float(string='Monto/Cambio',help='Monto dejado para cambio')    
    date = fields.Date(string='Fecha', required=True, index=True, default=fields.Date.context_today, help='Ingrese la fecha del monto entregado')               
    note = fields.Text(string='Nota',help='Describa Monto de Caja')
    state = fields.Selection([        
        ('pending', 'Pendiente'),                
        ('closed', 'Cerrado')
        ], 'Estado', default='pending', readonly=True,
        help='Indica el estado de la Transaccion',
        track_visibility="onchange",
        copy=False)
    active = fields.Boolean('Activo', default=True);
    detailchange_ids = fields.One2many(
        'lccash.detailchange', 'change_id', 'Cambio',
        )
    company_id = fields.Many2one('res.company', string='Company', required=True, readonly=True, default=lambda self: self.env['res.company']._company_default_get('lccash'))

    def closed(self):
        return self.write({'state':'closed'})
     
    def pending(self):
        return self.write({'state':'pending'})
  
class LcCashMoney(models.Model):
    _name = 'lccash.money'
    _description = 'Cortes de Moneda'
    
    currency_id = fields.Many2one('res.currency','Moneda',default=lambda self: self.env['res.currency'].search([('name', '=', 'BOB' )]).id)     
    name = fields.Char(string='Corte',help='Escriba el nombre del corte de la Moneda')
    active = fields.Boolean('Activo', default=True);

class LcCashDetailChange(models.Model):
    _name = 'lccash.detailchange'
    _description = 'Detalle del Cambio'
    _order = 'name desc'
        
    change_id = fields.Many2one('lccash.change','Cambio',required=True)    
    name = fields.Many2one('lccash.money','Moneda',required=True)
    cant = fields.Integer('Cantidad',help='Cantidad de Monedas',required=True)
    note = fields.Text(string='Nota',help='Notas y Series')