# -*- coding: utf-8 -*-

from odoo import models, fields, api, tools

class LcStockDataView(models.Model):
    _name = "lc.view.stock.data"
    _auto = False

    # product_id = fields.Integer('Product')
    warehouse_id = fields.Char('Warehouse')
    company_id = fields.Char('Company')
    location_id = fields.Char('Location')
    category = fields.Char('Category')
    default_code = fields.Char('Default Code')
    product_name = fields.Char('Name')
    list_price = fields.Float('Price')
    quantity = fields.Float('Quantity')
    cost = fields.Float('Cost')
    total = fields.Float('Total Cost')
     
    def init(self):        
        tools.drop_view_if_exists(self._cr, 'lc_view_stock_data')        
        self._cr.execute("""        
          CREATE VIEW lc_view_stock_data AS
            WITH stock_data AS (
              SELECT 
                w.id AS warehouse_id,
                w.company_id,
                l.id AS location_id,
                s.product_id,
                s.quantity
              FROM stock_warehouse w
              JOIN stock_location l ON w.lot_stock_id = l.id
              JOIN stock_quant s ON l.id = s.location_id
              WHERE 
                l.active = TRUE
                AND s.quantity > 0
            ),
            product_costs AS (
              SELECT 
                company_id,
                CAST(SUBSTR(ir_property.res_id::text, 17) AS INTEGER) AS id,
                ir_property.value_float AS cost
              FROM ir_property
              WHERE ir_property.res_id::text LIKE 'product.product,%'
            ),
            product_info_ranked AS (
              SELECT 
                c.company_id,
                t.id AS template_id,
                p.id AS product_id,
                p.default_code,
                r.name AS category,
                t.name AS product_name,
                t.list_price,
                COALESCE(c.cost, 0) AS cost,
                t.active,
                ROW_NUMBER() OVER (
                  PARTITION BY p.id
                  ORDER BY 
                    CASE 
                      WHEN c.company_id = 1 THEN 1
                      WHEN c.company_id = 2 THEN 2
                      WHEN c.company_id = 3 THEN 3
                      ELSE 4
                    END
                ) AS rn
              FROM product_product p
              JOIN product_template t ON p.product_tmpl_id = t.id
              LEFT JOIN product_costs c ON p.id = c.id
              LEFT JOIN product_category r ON t.categ_id = r.id 
              WHERE p.active=true
            ),
            product_info AS (
              SELECT *
              FROM product_info_ranked
              WHERE rn = 1 -- Solo el registro prioritario por product_id
            )
            SELECT 
              b.product_id AS id,
              a.warehouse_id,
              a.company_id,
              a.location_id,
              b.category,
              b.default_code,
              b.product_name,
              b.list_price,
              a.quantity,
              b.cost,
              ROUND((a.quantity * b.cost)::numeric, 2) AS total,
              b.active
            FROM stock_data a
            JOIN product_info b ON a.product_id = b.product_id;
          """
        )