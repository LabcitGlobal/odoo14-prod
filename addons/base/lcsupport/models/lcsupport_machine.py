# -*- coding: utf-8 -*-

from odoo import models, fields, api

class lcsupport(models.Model):
    _name = 'lcsupport.machine'
    _description = 'Descripcion del equipo'
    _order = 'create_date asc'
    
    @api.model
    def _get_default_machine_code(self):
        return self.env['ir.sequence'].next_by_code('machine.code')    
    
    client_id = fields.Many2one('res.partner','Cliente',required=True)
    category_id = fields.Many2one('product.category','Categoria',required=True)
    brand_id = fields.Many2one('lcsupport.brand','Marca',required=True)
    name = fields.Char(string='Equipo',required=True,help='Ingrese la descripcion del Equipo Electronico')
    model = fields.Char(string='Modelo',help='Describa el modelo')
    factory_series = fields.Char(string='Serie de Fabricacion',help='Numero de Serie de Fabrica')
    observation = fields.Text(string='Observaciones',help='ESpecifique si el equipo presenta alguna observacion')    
    detailmachine_ids = fields.One2many(
        'lcsupport.detailmachine', 'machine_id', 'Parte',
        )
    machine_code = fields.Char(string='Cod. Maquina', index=True, help='Codigo de Maquina',
                               default=_get_default_machine_code, copy=False)
    _sql_constraints = [
        ('lcsupport_machine__machine_code__uniq',
         'unique (machine_code)',
         'Codigo de Maquina Unico!'),
    ]
    
    #@api.multi
    #def action_set_machine_code(self):
    #    for machine in self:
    #        if not machine.machine_code:
    #            machine.write({
    #                'machine_code': self._get_default_machine_code(),
    #            })
    #    return True

class lcsupportbrand(models.Model):
    _name = 'lcsupport.brand'
    _description = 'Descripcion del equipo'
    _order = 'name asc'
    
    name = fields.Char('Marca',help='Nombre de la Marca',required=True)
    
class lcsupportunit(models.Model):
    _name = 'lcsupport.unit'
    _description = 'Unidad de Capacidad'
    _order = 'name asc'
    
    name = fields.Char('Unidad',help='Nombre de la Unidad',required=True)
    name_abbreviation = fields.Char('Abreviacion',help='Siglas de la Unidad',required=True)

class lcsupportdetailmachine(models.Model):
    _name = 'lcsupport.detailmachine'
    _description = 'Caracteristicas Tecnicas del Equipo'
    _order = 'name asc'
    
    name = fields.Char(string='Caracteristica',required=True,help='Ingrese la caracteristica tecnica del Equipo')
    capacity = fields.Float(string='Capacidad',required=True,help='Capacidad de la caracteristica')
    unit_id = fields.Many2one('lcsupport.unit','Unidad',required=True)
    serie = fields.Char(string='Serie',help='Numero de Serie de Fabrica')
    machine_id = fields.Many2one(
        'lcsupport.machine', 'Parte',
         ondelete='cascade')