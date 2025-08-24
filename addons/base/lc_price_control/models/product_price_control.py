# -*- coding: utf-8 -*-

from odoo import models, fields, api, tools

class lcProductPriceControlView(models.Model):
    _name = "lc.product.price.error.view"    
    _order = "name asc"
    _auto = False

    product_tmpl_id = fields.Many2one('product.template','Product ID')
    name = fields.Char('Product')
    price = fields.Float('Price')
    cost = fields.Float('Cost')
    fixed_price = fields.Float('Fixed Price')    
        
    def init(self):        
        tools.drop_view_if_exists(self._cr, 'lc_product_price_view')        
        self._cr.execute("""        
            CREATE VIEW lc_product_price_view AS
                SELECT 
                	t.id,
                	p.id AS product_id,
                    t.list_price AS price,
                    CASE
                    	WHEN c.cost > 0::double precision THEN c.cost
                        ELSE 0::double precision
                    END AS cost
                FROM product_template t
                LEFT JOIN product_product p ON t.id = p.product_tmpl_id
                LEFT JOIN ( SELECT substr(ir_property.res_id::text, 17, 8)::integer AS id,
                           ir_property.value_float AS cost
                           FROM ir_property WHERE ir_property.res_id::text ~~ '%product.product%'::text) c ON p.id = c.id
                WHERE t.active=true AND p.active=true
        """)

        tools.drop_view_if_exists(self._cr, 'lc_product_price_error_view')
        self._cr.execute("""        
            CREATE VIEW lc_product_price_error_view AS 
            SELECT DISTINCT 
                t.id, 
                t.id AS product_tmpl_id, 
                t.name, 
                ROUND(CAST(v.cost AS NUMERIC),2) AS cost, 
                v.price, 
                p.fixed_price
            FROM lc_product_price_view AS v, product_pricelist_item AS p, product_template t 
            WHERE v.id=p.product_tmpl_id
            AND v.id=t.id
            AND (v.cost >= v.price OR v.cost >= p.fixed_price)
            AND t.active=true
        """)