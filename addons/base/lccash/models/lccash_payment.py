# -*- coding: utf-8 -*-

from datetime import date, datetime
from odoo import models, fields, api

class LcCashPayment(models.Model):
    _name = 'lccash.payment'
    _description = 'Modelo para gestion de Depositos'
    _order = 'id desc'
             
    date = fields.Date(string='Fecha', required=True, index=True, default=fields.Date.context_today, help='Ingrese la fecha del Pago')    
    mount = fields.Float(string='Monto',help='Monto total de la Transaccion ')
    paid = fields.Float(string='Pago',help='Monto Pagado')     
    change = fields.Float(string='Cambio',help='Cambio Entregado')
    partner_id = fields.Many2one('res.partner','Cliente')
    employee_id = fields.Many2one('hr.employee','Empleado')
    name = fields.Many2one('pos.order','Pos')
    sale_id = fields.Many2one('sale.order','Venta')
    note = fields.Text(string='Nota',help='Describa Monto de Caja')
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
    detailpayment_ids = fields.One2many(
        'lccash.detailpayment', 'payment_id', 'Pago',
        )
    company_id = fields.Many2one('res.company', string='Company', required=True, readonly=True, default=lambda self: self.env['res.company']._company_default_get('lccash'))

    def closed(self):
        return self.write({'state':'closed'})
     
    def pending(self):
        return self.write({'state':'pending'})
    
    @api.onchange('name')
    def _onchange_name(self):
        self.mount = self.name.amount_total
        self.paid = self.name.amount_total
    
    @api.model
    def create(self,values):
        val = {}        
        payment_line = self.env['lccash.payment'].search([('name','=',values['name'])])
        payment_total = sum(payline.paid for payline in payment_line)
        val['payment'] = payment_total + values['paid']       
        pos_record = self.env['pos.order'].search([('id','=',values['name'])])
        pos_record.write(val)
        record = super(LcCashPayment, self).create(values)
        return record
        
    # @api.multi
    def write(self,values):
        val = {}
        payment_ok = self.env['lccash.payment'].search([('id','=',self.id)])
        payment_line = self.env['lccash.payment'].search([('name','=',self.name.id)])
        payment_total = sum(payline.paid for payline in payment_line) 
        if 'paid' in values:           
            val['payment'] = payment_total - payment_ok['paid'] + values['paid']               
            pos_record = self.env['pos.order'].search([('id','=',self.name.id)])
            pos_record.write(val)
        record = super(LcCashPayment, self).write(values)
        return record
       
    
class LcCashDetailPayment(models.Model):
    _name = 'lccash.detailpayment'
    _description = 'Detalle del Pago'
    _order = 'name desc'
        
    payment_id = fields.Many2one('lccash.payment','Pago',required=True)    
    name = fields.Many2one('lccash.money','Moneda',required=True)
    cant = fields.Integer('Cantidad',help='Cantidad de Monedas',required=True)
    note = fields.Text(string='Nota',help='Notas y Series')