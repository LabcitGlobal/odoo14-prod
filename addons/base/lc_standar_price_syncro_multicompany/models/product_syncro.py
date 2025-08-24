# -*- coding: utf-8 -*-

from odoo import models, fields, api, tools


class lcStandarPriceSyncroProductProduct(models.Model):
    _inherit = "product.product"

    @api.model
    def init(self):        
        self._cr.execute("""        
            DELETE FROM ir_property 
            		 WHERE ir_property.res_id::text ~~ '%product.product%'::text 
            		 AND name='standard_price'
					 AND company_id>1
        """)
        self._cr.execute("""        
            UPDATE ir_property SET company_id=null 
            		 WHERE ir_property.res_id::text ~~ '%product.product%'::text 
            		 AND name='standard_price'
        """)
        
    def write(self, vals):
        res = super().write(vals)        
        for item in self:            
            if("standard_price" in vals):
                self.env.cr.execute("UPDATE ir_property SET value_float={} WHERE ir_property.res_id::text ~~ '%product.product%'::text AND name='standard_price' AND SPLIT_PART(res_id,',',2)::integer={}".format(vals["standard_price"],item.id))            
        return res

class lcStandarPriceSyncroProductTemplate(models.Model):
    _inherit = "product.template"

    def copy_standard_price_multicompany(self):
        sql = """
            INSERT INTO ir_property(name, res_id, company_id, fields_id, value_float, type, create_uid, create_date, write_uid, write_date)
            SELECT i.name, i.res_id, c.company_id, i.fields_id, i.value_float, i.type, i.create_uid, i.create_date, i.write_uid, i.write_date 
            FROM 
            	ir_property i, 
            	(SELECT id AS company_id FROM res_company WHERE id NOT IN(
            		 SELECT DISTINCT company_id FROM ir_property 
            		 WHERE ir_property.res_id::text ~~ '%product.product%'::text 
            		 AND name='standard_price' 
            		 AND split_part(res_id,',',2)::integer = (SELECT id FROM product_product WHERE product_tmpl_id={product_tmpl_id}))
            	) AS c
            WHERE i.res_id::text ~~ '%product.product%'::text 
            AND i.name='standard_price' 
            AND split_part(i.res_id,',',2)::integer = (SELECT id FROM product_product WHERE product_tmpl_id={product_tmpl_id})
        """.format(product_tmpl_id=self.id)
        self.env.cr.execute(sql)
        # print(sql)