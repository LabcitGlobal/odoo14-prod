from odoo import models, fields, tools


class StockQuantProductTemplateMulti(models.Model):
    _name = 'view.stock.quant.multicompany'
    _order = 'location_name desc' 
    _auto = False
    
    product_tmpl_id = fields.Many2one('product.template', string="Product Template") 
    product_id = fields.Many2one('product.product', string="Product Product") 
    name = fields.Char(string="Product Name")
    default_code = fields.Char(string="Default Code")
    company_name = fields.Char(string="Company")
    location_name = fields.Char(string="Location")
    quantity = fields.Float(string="Quantity")

    def init(self):
        tools.drop_view_if_exists(self._cr, 'lccommission_posagent_view')
        self._cr.execute("""
            create or replace view view_stock_quant_multicompany as (
            	select
                    s.id, 
            		t.id as product_tmpl_id, 
            		s.product_id, 
            		t.name, 
            		p.default_code, 
            		c.name as company_name, 
            		l.complete_name as location_name, 
            		s.quantity 
            	from stock_quant s, res_company c, stock_location l, product_product p, product_template t 
            	where s.company_id=c.id 
            	and s.location_id=l.id 
            	and s.product_id=p.id 
            	and p.product_tmpl_id=t.id 
            	and s.location_id in (
            		select id from stock_location 
            		where id in (select distinct location_id from stock_quant where company_id is not null) 
            		and usage='internal'
            	) order by location_name
            )
        """)