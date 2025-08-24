from odoo import api, fields, models, _

class ProductTemplate(models.Model):
    _inherit = "product.template"

    def _get_pricelist_item(self):        
        pricelist = self.env["product.pricelist.item"].search([('product_tmpl_id','=',self.id),('web_enabled','=','true')], order="pricelist_id, min_quantity desc")
        # for item in pricelist:
        #     print("{item.pricelist_id.name} {item.min_quantity} {item.fixed_price}")
        return pricelist
