# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from datetime import datetime,date
import base64                               
from odoo.exceptions import UserError, ValidationError


class ProductCatalog(models.TransientModel):
	_name = 'lc.product.catalog'
	_description="Product Catalog Style"

	@api.onchange('description')
	def set_boolean_configurations(self):
		for rec in self:
			if rec.report_style == 'style_2' and rec.description == False:
				raise ValidationError("Description is Required for Style 2.")


	catalog_type = fields.Selection(
		[('product', 'Product'), ('category', 'Category')],
		string='Catalog Type',
		default='product')
	product_ids=fields.Many2many('product.product',string="Products")
	categories_ids=fields.Many2many('product.category',string="Categories")
	image_size = fields.Selection(
		[('small', 'Small'), ('medium', 'Medium'),('large', 'Large')],
		string='Image Size',
		default='small')
	currency_id = fields.Many2one('res.currency', default=lambda self: self.env.company.currency_id.id,string="Currency")
	price = fields.Boolean(default=False,string="Price")
	report_style = fields.Selection(
		[('style_1', 'Style 1'),
		('style_2', 'Style 2'),
		('style_3', 'Style 3'),
		('style_4', 'Style 4'),
		('style_5', 'Style 5'),
		('style_6', 'Style 6 Watermark') ],
		string='Style',
		default='style_1')
	description = fields.Boolean(default=False,string="Description")
	print_box_per_row = fields.Selection(
		[('two_box_per_row', '2 box per row'),
		('three_box_per_row', '3 box per row'),
		('four_box_per_row', '4 box per row')],
		string='Print box per row',
		default='two_box_per_row')
	category_name = fields.Boolean(default=False,string="Category Name")
	image_check = fields.Boolean(default=True,string="With Image")
	pdf_watermark = fields.Boolean(default=False,string="Watermark")
	quant_stock_check = fields.Boolean(default=False,string="Quant  Available > 0")



	@api.onchange('catalog_type')
	def _onchange_catalog_type(self):
		if self.catalog_type == 'product':
			self.categories_ids = False
		else:
			self.product_ids = False


	def print_style_catalog(self):		
		if self.report_style == 'style_1':
			[data] = self.read()
			datas = {
				 'ids': [1],
				 'model': 'lc.product.catalog',
				 'form': data
			}
			action = self.env.ref('lc_product_catalog.action_report_product_catalog_style_1').\
				report_action(self, data=datas)
			action.update({'close_on_report_download': True})			
			return action

		elif self.report_style == 'style_2':
			[data] = self.read()
			datas = {
				 'ids': [1],
				 'model': 'lc.product.catalog',
				 'form': data
			}
			action = self.env.ref('lc_product_catalog.action_report_product_catalog_style_2').\
				report_action(self, data=datas)
			action.update({'close_on_report_download': True})			
			return action

		elif self.report_style == 'style_3':
			[data] = self.read()
			datas = {
				 'ids': [1],
				 'model': 'lc.product.catalog',
				 'form': data
			}
			action = self.env.ref('lc_product_catalog.action_report_product_catalog_style_3').\
				report_action(self, data=datas)
			action.update({'close_on_report_download': True})			
			return action

		elif self.report_style == 'style_4':
			[data] = self.read()
			datas = {
				 'ids': [1],
				 'model': 'lc.product.catalog',
				 'form': data
			}
			action = self.env.ref('lc_product_catalog.action_report_product_catalog_style_4').\
				report_action(self, data=datas)
			action.update({'close_on_report_download': True})			
			return action

		elif self.report_style == 'style_5':
			[data] = self.read()
			datas = {
				 'ids': [1],
				 'model': 'lc.product.catalog',
				 'form': data
			}
			action = self.env.ref('lc_product_catalog.action_report_product_catalog_style_5').\
				report_action(self, data=datas)
			action.update({'close_on_report_download': True})			
			return action
		
		elif self.report_style == 'style_6':
			[data] = self.read()
			datas = {
				 'ids': [1],
				 'model': 'lc.product.catalog',
				 'form': data
			}
			action = self.env.ref('lc_product_catalog.action_report_product_catalog_style_6').\
				report_action(self, data=datas)
			action.update({'close_on_report_download': True})			
			return action

