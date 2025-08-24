# -*- coding: utf-8 -*-

from odoo import models, fields, api

class lc_stock_employee(models.Model):
      _name = 'lc_stock_employee'

      def _get_employee_id(self):
        employee_rec = self.env['hr.employee'].search([('user_id', '=', self.env.uid)], limit=1)
        return employee_rec.id

      name = fields.Many2one('hr.employee','Responsable', default=_get_employee_id)
      categ_id = fields.Many2one('product.category','Categoria')
      company_id = fields.Many2one('res.company', string='Company', required=True, readonly=True, default=lambda self: self.env['res.company']._company_default_get('lc_stock_employee'))
