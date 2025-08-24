# -*- coding: utf-8 -*-

from odoo import models, fields, api

class lc_stock_employee_report(models.TransientModel):
      _name = 'lc_stock_employee_report'

      def _get_employee_id(self):
        employee_rec = self.env['hr.employee'].search([('user_id', '=', self.env.uid)], limit=1)
        return employee_rec.id

      employee_id = fields.Many2one('hr.employee',string="Employee", default=_get_employee_id)

    #   @api.multi
      def print_stock_report(self):
        datas = []
        domain = []               
        if self.employee_id:
            domain.append(('id', '=', self.employee_id.ids))        
        employee = self.env['hr.employee'].search([('id','=',self.employee_id.ids[0])])
        
        # allowed_companies = self.env.user.company_ids
        # print(allowed_companies)  # Cambiado a company_ids
        # print(self.env.company.id)
        # company_id = allowed_companies[0].id if allowed_companies else False
        
        sql_query = """
            SELECT p.id AS product_id, w.code AS location, p.default_code, t.name, s.quantity 
            FROM product_product p, product_template t, stock_quant s, stock_location l, stock_warehouse w 
            WHERE p.product_tmpl_id=t.id AND p.id=s.product_id AND s.location_id=l.id AND l.id=w.lot_stock_id AND p.active='t' AND s.company_id=%s AND w.active='t'
            AND t.categ_id IN (
               WITH RECURSIVE CTE AS (
	               SELECT id FROM product_category WHERE id IN (SELECT categ_id FROM lc_stock_employee WHERE name=%s)
	               UNION ALL
	               SELECT t.id FROM product_category t INNER JOIN CTE c ON t.parent_id=c.id
               )
               SELECT * FROM CTE
            ) ORDER BY code, name;
        """ % (self.env.company.id,self.employee_id.ids[0])
        # print(sql_query)
        self.env.cr.execute(sql_query)
        result = self.env.cr.dictfetchall()        
        for reg in result:              
            datas.append({
                'product_id':reg['product_id'],
                'location': reg['location'],                
                'default_code':reg['default_code'],
                'product_name':reg['name'],
                'quantity':reg['quantity'],                
            })                        
        
        res = {
            'stock':datas,            
            'employee': employee.name,            
        }
        data = {
            'form': res,
        }
        return self.env.ref('lc_stock_employee.lc_stock_employee_report_print').report_action([],data=data)

