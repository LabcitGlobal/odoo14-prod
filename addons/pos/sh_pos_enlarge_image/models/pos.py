# Part of Softhealer Technologies.

from odoo import models, fields


class PosConfig(models.Model):
    _inherit = 'pos.config'

    sh_enable_image = fields.Boolean('Enable Enlarge Image')
    sh_enable_stock_multicompany = fields.Boolean('Enable View Stock Quant')


class stock_quant(models.Model):
    _inherit = 'stock.quant'

    def get_single_product_multicompany(self, product):
        res = []
        pro = self.env['product.product'].browse(product)		
        quants = self.env['stock.quant'].search([('product_id', '=', pro.id),('company_id','!=',False),('quantity', '>=', 0)])
        if len(quants) > 1:
            quantity = 0.0
            for quant in quants:
                quantity += quant.quantity
            res.append([pro.id, quantity])
        else:
            res.append([pro.id, quants.quantity])
        return res
    

    def get_single_product_company(self, product):        
        datas = []
        pro = self.env['product.product'].browse(product)
        sql_query = """
            select s.product_id, c.name as company_name, l.complete_name as location_name, s.quantity from stock_quant s, res_company c, stock_location l where s.product_id=%s and s.company_id=c.id and s.location_id=l.id and s.location_id in (
	            select id from stock_location 
	            where id in (select distinct location_id from stock_quant where company_id is not null) 
	            and usage='internal'
            );
        """ % (pro.id)
        self.env.cr.execute(sql_query)
        result = self.env.cr.dictfetchall()        
        for reg in result:              
            datas.append({
                'product_id':reg['product_id'],
                'company_name':reg['company_name'],
                'location_name': reg['location_name'],
                'quantity':reg['quantity'],                
            })                        
        
        return datas