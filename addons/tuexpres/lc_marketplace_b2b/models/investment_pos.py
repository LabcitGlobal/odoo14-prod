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

class InvestmentPosView(models.Model):
    _name = "lc.investment.pos.view"
    _auto = False    
    
    marketplace_seller_id = fields.Many2one('res.partner',string="Seller")
    seller_commision = fields.Float(string="Seller Commission")    
    product_id = fields.Many2one('product.product',string="Product")    
    create_date = fields.Date(string="Date")
    name = fields.Char(string="Product")
    price_unit = fields.Float(string="Price")
    purchase_price = fields.Float(string="Purchase")
    qty = fields.Float(string="Quantity")
    price_subtotal = fields.Float(string="Price Subtotal")
    margin = fields.Float(string="Margin")
    commission = fields.Float(string="Commission")
    investment = fields.Float(string="Investment")

    def init(self):        
        tools.drop_view_if_exists(self._cr, 'lc_investment_pos_view')        
        self._cr.execute("""        
            CREATE OR REPLACE VIEW lc_investment_pos_view AS 
            SELECT 
            	o.id, 
                t.marketplace_seller_id, 
            	r.seller_commission, 
            	o.product_id, 
            	o.create_date::timestamp at time zone 'UTC' AS create_date, 
            	o.full_product_name as name, 
            	o.price_unit, 
            	o.purchase_price, 
            	o.qty, 
            	o.price_subtotal, 
            	o.margin, 
            	ROUND((o.margin*r.seller_commission)::numeric,2) AS commission, 
            	ROUND((o.qty*o.purchase_price)::numeric,2) AS investment 
            FROM pos_order_line o LEFT JOIN product_product p ON o.product_id=p.id 
            LEFT JOIN product_template t ON p.product_tmpl_id=t.id 
            LEFT JOIN res_partner r ON t.marketplace_seller_id=r.id
        """)