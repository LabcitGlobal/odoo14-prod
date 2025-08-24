# -*- coding: utf-8 -*-

from odoo import models, fields, api

class lcStockDataReport(models.TransientModel):
      _name = 'lc.stock.data.report'
      
      # @api.multi
      def print_stock_report(self):
        datas = []
        domain = []               
        
        # allowed_companies = self.env.user.company_ids
        # print(allowed_companies)  # Cambiado a company_ids
        # print(self.env.company.id)
        # company_id = allowed_companies[0].id if allowed_companies else False
        
        sql_query = """
            SELECT id, product_name, default_code, quantity FROM lc_view_stock_data WHERE company_id=%s ORDER BY product_name;
        """ % (self.env.company.id)
        # print(sql_query)
        self.env.cr.execute(sql_query)
        result = self.env.cr.dictfetchall()        
        for reg in result:              
            datas.append({
                'product_id':reg['id'],
                'product_name': reg['product_name'],                
                'default_code':reg['default_code'],
                'quantity':reg['quantity'],                
            })                        
        
        res = {
            'stock':datas,                        
        }
        data = {
            'form': res,
        }
        return self.env.ref('lc_stock_data.lc_stock_data_report_print').report_action([],data=data)
      
      # @api.multi
      def print_stock_cost_report(self):
        datas = []
        domain = []               
        
        # allowed_companies = self.env.user.company_ids
        # print(allowed_companies)  # Cambiado a company_ids
        # print(self.env.company.id)
        # company_id = allowed_companies[0].id if allowed_companies else False
        
        sql_query = """
            SELECT id, product_name, default_code, cost, quantity, total FROM lc_view_stock_data WHERE company_id=%s ORDER BY product_name;
        """ % (self.env.company.id)
        # print(sql_query)
        self.env.cr.execute(sql_query)
        result = self.env.cr.dictfetchall()        
        total = 0
        for reg in result:              
            total = total + reg['total']
            datas.append({
                'product_id':reg['id'],
                'product_name': reg['product_name'],                
                'default_code':reg['default_code'],
                'cost':reg['cost'],
                'quantity':reg['quantity'],                
                'total':reg['total'],                
            })                        
        
        res = {
            'stock':datas,                        
            'total':round(total,2),            
        }
        data = {
            'form': res,
        }
        return self.env.ref('lc_stock_data.lc_stock_data_cost_report_print').report_action([],data=data)
      
      


