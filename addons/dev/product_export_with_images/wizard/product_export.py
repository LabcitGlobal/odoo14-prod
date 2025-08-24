# -*- coding: utf-8 -*-
#############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2024-TODAY Cybrosys Technologies(<https://www.cybrosys.com>)
#    Author: Ammu Raj(odoo@cybrosys.com)
#
#    You can modify it under the terms of the GNU AFFERO
#    GENERAL PUBLIC LICENSE (AGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU AFFERO GENERAL PUBLIC LICENSE (AGPL v3) for more details.
#
#    You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
#    (AGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################
from odoo import fields, models
from odoo.http import request


class ExportWizard(models.TransientModel):
    """This class contains the functions to get selected product ids and
    redirect to excel download URL .
    Methods:
        action_export_products():
            calls URL action to download excel report.
        get_product_lines():
             return selected product details.
    """

    _name = "product.export"
    _description = "Export Products and Make an Excel Download URL."

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
        return URL action to download excel report.
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
                "url": "/products_download/excel_report/%s" % export_wizard.id,
                "target": "new",
                "context": {"active_ids": active_products},
            }

    def get_product_lines(self):
        """
        returns the product details like name, default code, category, image etc.
        """
        rec_list = []
        if self.product_ids:            
            for rec in self.product_ids:            
                vals = {
                    "name": rec.name,
                    "internal_reference": rec.default_code,
                    "category": rec.categ_id.display_name,
                    "currency": self.env.company.currency_id.symbol,
                    "cost": rec.standard_price,
                    "sales_price": rec.list_price,
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
                                "category": rec.categ_id.display_name,
                                "currency": self.env.company.currency_id.symbol,
                                "cost": rec.standard_price,
                                "sales_price": rec.list_price,
                                "image": image.image_1920,
                            }                        
                            rec_list.append(vals)

        elif self.product_tmp_ids:
            for rec in self.product_tmp_ids:            
                vals = {
                    "name": rec.name,
                    "internal_reference": rec.default_code,
                    "category": rec.categ_id.display_name,
                    "currency": self.env.company.currency_id.symbol,
                    "cost": rec.standard_price,
                    "sales_price": rec.list_price,
                    "image": rec.image_1920,
                }
                rec_list.append(vals)

                # Busca si tiene imagenes asociadas a la plantilla del producto
                if rec.product_template_image_ids:
                    print("Entro image_ids")
                    for image in rec.product_template_image_ids:
                        if image.image_1920:
                            vals = {
                                "name": rec.name,
                                "internal_reference": rec.default_code,
                                "category": rec.categ_id.display_name,
                                "currency": self.env.company.currency_id.symbol,
                                "cost": rec.standard_price,
                                "sales_price": rec.list_price,
                                "image": image.image_1920,
                            }                        
                            rec_list.append(vals)
                
                variants = request.env['product.product'].search([('product_tmpl_id', 'in', self.product_tmp_ids.ids)])
                if variants and len(variants) > 1:
                    print("Entro variants")
                    for variant in variants:
                        vals = {
                            "name": variant.name,
                            "internal_reference": variant.default_code,
                            "category": variant.categ_id.display_name,
                            "currency": self.env.company.currency_id.symbol,
                            "cost": variant.standard_price,
                            "sales_price": variant.list_price,
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
                                        "category": variant.categ_id.display_name,
                                        "currency": self.env.company.currency_id.symbol,
                                        "cost": variant.standard_price,
                                        "sales_price": variant.list_price,
                                        "image": image.image_1920,
                                    }                        
                                    rec_list.append(vals)
        return rec_list
