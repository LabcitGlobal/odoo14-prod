# -*- coding: utf-8 -*-

from odoo import models, fields, api
from dateutil.relativedelta import relativedelta

class lcsupportservice(models.Model):
    _name = 'lcsupport.service'
    _description = 'Servicios Realizados'
    _order = 'date_reception desc'
    
    def compute_next_day_date(self, strdate):
        oneday = relativedelta(days=1)
        start_date = fields.Date.from_string(strdate)
        return fields.Date.to_string(start_date + oneday)
    
    machine_id = fields.Many2one('lcsupport.machine','Equipo',required=True)
    name = fields.Many2one('res.partner','Cliente',required=True)
    employee_id = fields.Many2one('hr.employee','Tecnico',required=True)    
    date_reception = fields.Datetime(string='Recepcion', default=fields.Datetime.now, required=True,help='Ingrese la descripcion del Equipo Electronico')
    date_delivery = fields.Datetime(string='Entrega', default=lambda self:
        self.compute_next_day_date(fields.Date.context_today(self)), help='Seleccione el dia y hora de entrega')
    technical_diagnosis = fields.Text(string='Diagnostico Tecnico',help='Que problema presenta el equipo')
    customer_problem = fields.Text(string='Problema (Cliente)',help='Problema que indica el cliente')
    accessories = fields.Text(string='Accesorios Dejados',help='Describa que accesorios esta dejando (Cables, Cobertores, Cajas, etc.)')
    solution = fields.Text(string='Solucion Final',help='Describa la solucion que se dio al diagnostico')     
    price = fields.Float(string='Precio',help='Precio estimado a ser cobrado')
    tax = fields.Boolean(string='Impuestos',help='Marque si el servicio se emitio factura')
    detailservice_ids = fields.One2many(
        'lcsupport.detailservice', 'service_id', 'Servicio',
        )    
    state = fields.Selection([        
        ('pending', 'Pendiente'),
        ('expired', 'Expirado'),        
        ('closed', 'Finalizado')
        ], 'Estado', default='pending', readonly=True,
        help='Indica el estado en el que se encuentra el servicio',
        track_visibility="onchange",
        copy=False)
    active = fields.Boolean('Activo', default=True);
    company_id = fields.Many2one('res.company', string='Company', required=True, readonly=True, default=lambda self: self.env['res.company']._company_default_get('lcsupport'))
    
    def expire(self):
        return self.write({'state':'expired'})        
    
    def close(self):
        return self.write({'state':'closed'})
    
    def pendin(self):
        return self.write({'state':'pending'})        
    
    # @api.multi
    def print_repair_order(self):
        return self.env.ref('lcsupport.service.action_report_service_order').report_action(self)

class lcsupportservicecategory(models.Model):
    _name = 'lcsupport.servicecategory'
    _description = 'Categoria del Servicio'
    _order = 'name asc'
    
    name = fields.Char('Categoria',help='Nombre de la Categoria',required=True)
    
class lcsupportservicetype(models.Model):
    _name = 'lcsupport.servicetype'
    _description = 'Tipo de Servicio'
    _order = 'name asc'
    
    servicecategory_id = fields.Many2one('lcsupport.servicecategory','Categoria',required=True)
    name = fields.Char('Servicio',help='Nombre del Servicio',required=True)
    price = fields.Float('Precio',help='Precio del Servicio',required=True)

class lcsupportdetailservice(models.Model):
    _name = 'lcsupport.detailservice'
    _description = 'Detalle del Servicio'
    _order = 'name asc'
        
    service_id = fields.Many2one('lcsupport.service','Servicio',required=True)
    name = fields.Many2one('lcsupport.servicetype','Servicio',required=True)
    price = fields.Float('Precio',help='Precio del Servicio',required=True)