# -*- coding: utf-8 -*-

from odoo import fields, models
from odoo.http import request


class ExportWizard(models.TransientModel):
    """This class contains the functions to get selected product ids and
    redirect to export download URL .
    Methods:
        action_export_products():
            calls URL action to download excel report.
        get_product_lines():
             return selected product details.
    """

    _name = "product.export"
    _description = "Export Images from Products."

    name = fields.Char(string="Name", help="Name of the record")
    product_tmp_ids = fields.Many2many(
        "product.template", string="Products", help="Products for exporting"
    )

    product_ids = fields.Many2many(
        "product.product", string="Products", help="Product variants for exporting"
    )

    def action_export_products(self):
        """
        select the active product/ product template ids.
        return URL action to zip download.
        """
        active_products = self.env.context["active_ids"]
        active_model = self.env.context["active_model"]
        if active_model == "product.template":
            export_wizard = self.env["product.export"].create(
                {"product_tmp_ids": [(6, 0, active_products)]}
            )
        if active_model == "product.product":
            export_wizard = self.env["product.export"].create(
                {"product_ids": [(6, 0, active_products)]}
            )
        if export_wizard:
            return {
                "type": "ir.actions.act_url",
                "url": "/products_download/image_zip/%s" % export_wizard.id,
                "target": "new",
                "context": {"active_ids": active_products},
            }

    def get_product_lines(self):
        """
        returns the product details like name, default code, image etc.
        """
        rec_list = []
        count = 0
        if self.product_ids:            
            for rec in self.product_ids:            
                vals = {
                    "name": rec.name,
                    "internal_reference": rec.default_code,                    
                    "image": rec.image_1920,
                }
                rec_list.append(vals)

                # Busca si tiene imagenes asociadas a la variante del producto
                if rec.product_variant_image_ids:
                    for image in rec.product_variant_image_ids:
                        if image.image_1920:
                            vals = {
                                "name": rec.name,
                                "internal_reference": rec.default_code,                                            
                                "image": image.image_1920,
                            }                        
                            rec_list.append(vals)

        elif self.product_tmp_ids:            
            for rec in self.product_tmp_ids:                
                # TODO: Comentar esta parte si no se quiere exportar la imagen de la plantilla
                #  del producto de forma que no se repita en el listado
                # vals = {
                #     "name": rec.name,
                #     "internal_reference": rec.default_code,                    
                #     "image": rec.image_1920,
                # }
                # rec_list.append(vals)

                # Busca si tiene imagenes asociadas a la plantilla del producto
                if rec.product_template_image_ids:                    
                    for image in rec.product_template_image_ids:
                        if image.image_1920:
                            vals = {
                                "name": rec.name,
                                "internal_reference": rec.default_code,                                            
                                "image": image.image_1920,
                            }                        
                            rec_list.append(vals)
                
                variants = request.env['product.product'].search([('product_tmpl_id', '=', rec.id)])                                
                # if variants and len(variants) > 1:
                if variants:
                    for variant in variants:
                        vals = {
                            "name": variant.name,
                            "internal_reference": variant.default_code,                           
                            "image": variant.image_1920,
                        }
                        rec_list.append(vals)

                        # Busca si tiene imagenes asociadas a la variante del producto
                        if variant.product_variant_image_ids:
                            for image in variant.product_variant_image_ids:
                                if image.image_1920:
                                    vals = {
                                        "name": variant.name,
                                        "internal_reference": variant.default_code,                                                   
                                        "image": image.image_1920,
                                    }                        
                                    rec_list.append(vals)
        print(f"Exporting {len(rec_list)} product images.")
        return rec_list
