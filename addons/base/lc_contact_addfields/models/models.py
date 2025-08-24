# -*- coding: utf-8 -*-

from odoo import models, fields, api

class partner_dni_bo(models.Model):
     _inherit = 'res.partner'
     
     date_birth = fields.Date(string="Date of Birth")
     ci = fields.Char(string="CI")
     emision = fields.Many2one('res.country.state', string='Issued',default=lambda self: self.env['res.country.state'].search([('code', '=', 'BO-L' )]).id)     
     zip = fields.Char(default="0591")
     city = fields.Char(default="El Alto")
     country_id = fields.Many2one('res.country',default=lambda self: self.env['res.country'].search([('code', '=', 'BO' )]).id)
     state_id = fields.Many2one('res.country.state', string='Department',default=lambda self: self.env['res.country.state'].search([('code', '=', 'BO-L' )]).id)
     district_id = fields.Many2one('res.country.district')    
     
     _sql_constraints = [('ci_emision_unique', 'unique(ci,emision)', "Error: Already registered customer!")]    
      
     """_defaults = { 
        'country_id': lambda self, cr, uid, context: self.pool.get('res.country').browse(cr, uid, self.pool.get('res.country').search(cr, uid, [('code','=','BO')]))[0].id,
        'state_id': lambda self, cr, uid, context: self.pool.get('res.country.state').browse(cr, uid, self.pool.get('res.country.state').search(cr, uid, [('code','=','BO-L')]))[0].id,
        'emision': lambda self, cr, uid, context: self.pool.get('res.country.state').browse(cr, uid, self.pool.get('res.country.state').search(cr, uid, [('code','=','BO-L')]))[0].id,
        'city': "El Alto",        
        }"""