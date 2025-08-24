# -*- coding: utf-8 -*-
#############################################################################
#
#    Labcit Inc.
#
#    Copyright (C) 2021-TODAY Labcit Inc. (<https://www.labcit.com>).
#    Author: Laboratorio en Tecnologias Tic @labcit(support@labcit.com)
#
#    You can modify it under the terms of the ALUF the Labcit Inc.
#
#############################################################################

from odoo import models, fields, api, tools

class InvestmentProductView(models.Model):
    _name = "lc.investment.product.view"
    _auto = False    
    
    name = fields.Many2one('product.product',string="Product")    
    marketplace_seller_id = fields.Many2one('res.partner',string="Customer")    
    quantity = fields.Float(string="Quantity")
    cost = fields.Float(string="Cost")
    investment = fields.Float(string="Investment")    

    def init(self):        
        tools.drop_view_if_exists(self._cr, 'lc_investment_product_view')        
        self._cr.execute("""        
            CREATE OR REPLACE VIEW lc_investment_product_view AS
            SELECT 
            	q.product_id AS id, 
            	q.product_id AS name, 
            	t.marketplace_seller_id, 
            	q.quantity, 
            	ROUND(c.cost::numeric,2) AS cost, 
            	ROUND((q.quantity*c.cost)::numeric,2) AS investment 
            FROM stock_quant q LEFT JOIN ( 
            	SELECT substr(ir_property.res_id::text, 17, 8)::integer AS id, ir_property.value_float AS cost
                FROM ir_property
                WHERE ir_property.res_id::text ~~ '%product.product%'::text AND company_id=1
            ) c ON q.product_id = c.id 
            LEFT JOIN product_product p ON q.product_id=p.id 
            LEFT JOIN product_template t ON p.product_tmpl_id=t.id 
            WHERE q.location_id=(SELECT id FROM stock_location WHERE active=true AND usage='internal' AND location_id=7)
        """)


