# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime

class LcCashWithdraw(models.Model):
    _name = 'lccash.withdraw'
    _description = 'Modelo para gestion de Retiros'
    _order = 'id desc'
    
    date = fields.Date(string='Fecha', required=True, index=True, default=fields.Date.context_today, help='Ingrese la fecha del Retiro')     
    name = fields.Float(string='Retiro',help='Monto Retirado')
    mount = fields.Float(string='Monto',help='Monto total de la Transaccion ')
    partner_id = fields.Many2one('res.partner','Proveedor/Cliente')
    employee_id = fields.Many2one('hr.employee','Empleado')
    purchase_id = fields.Many2one('purchase.order','Compra')     
    note = fields.Text(string='Nota',help='Describa Monto de Caja') 
    pos_id = fields.Many2one('pos.order','Pos')
    photo = fields.Image(string="Foto", max_width=800)
    file = fields.Binary(string="Archivo")
    payment_type = fields.Selection([
        ('cash','Efectivo'),
        ('check','Cheque'),
        ('bank','Banco')
    ], 'Payment Type', default="cash")
    payment_date = fields.Date(string="Payment Date", index=True, default=fields.Date.context_today) 
    bank = fields.Many2one('res.bank', string="Bank")
    transaction_code = fields.Char(string="Transaction")
    state = fields.Selection([        
        ('pending', 'Pendiente'),                
        ('closed', 'Cerrado')
        ], 'Estado', default='pending', readonly=True,
        help='Indica el estado de la Transaccion',
        track_visibility="onchange",
        copy=False)
    active = fields.Boolean('Activo', default=True);
    detailwithdraw_ids = fields.One2many(
        'lccash.detailwithdraw', 'withdraw_id', 'Retiro',
        )
    company_id = fields.Many2one('res.company', string='Company', required=True, readonly=True, default=lambda self: self.env['res.company']._company_default_get('lccash'))

    def closed(self):
        return self.write({'state':'closed'})
     
    def pending(self):
        return self.write({'state':'pending'})
    
    @api.onchange('purchase_id')
    def _onchange_name(self):
        self.name = self.purchase_id.amount_total
        self.mount = self.purchase_id.amount_total
    
    @api.model
    def create(self,values):
        val = {}
        payment_line = self.env['lccash.withdraw'].search([('purchase_id','=',values['purchase_id'])])
        payment_total = sum(payline.name for payline in payment_line)        
        val['payment'] = payment_total + values['name']       
        pos_record = self.env['purchase.order'].search([('id','=',values['purchase_id'])])
        pos_record.write(val)
        record = super(LcCashWithdraw, self).create(values)
        return record
        
    def write(self,values):
        val = {}
        payment_ok = self.env['lccash.withdraw'].search([('id','=',self.id)])
        payment_line = self.env['lccash.withdraw'].search([('purchase_id','=',self.purchase_id.id)])
        payment_total = sum(payline.name for payline in payment_line) 
        if 'name' in values:           
            val['payment'] = payment_total - payment_ok['name'] + values['name']               
            pos_record = self.env['purchase.order'].search([('id','=',self.purchase_id.id)])
            pos_record.write(val)
        record = super(LcCashWithdraw, self).write(values)
        return record

class LcCashDetailWithdraw(models.Model):
    _name = 'lccash.detailwithdraw'
    _description = 'Detalle del Retiro'
    _order = 'name desc'
        
    withdraw_id = fields.Many2one('lccash.withdraw','Retiro',required=True)    
    name = fields.Many2one('lccash.money','Moneda',required=True)
    cant = fields.Integer('Cantidad',help='Cantidad de Monedas',required=True)
    note = fields.Text(string='Nota',help='Notas y Series')