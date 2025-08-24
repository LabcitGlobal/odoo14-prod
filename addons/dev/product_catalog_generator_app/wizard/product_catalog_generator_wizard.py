# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from datetime import datetime,date
import base64                               
from odoo.exceptions import UserError, ValidationError


class ProductCatalog(models.TransientModel):
	_name = 'product.catalog'
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
	currency_id = fields.Many2one('res.currency',string="Currency")
	price = fields.Boolean(default=True,string="Price")
	report_style = fields.Selection(
		[('style_1', 'Style 1'),
		('style_2', 'Style 2'),
		('style_3', 'Style 3'),
		('style_4', 'Style 4'),
		('style_5', 'Style 5') ],
		string='Style',
		default='style_1')
	description = fields.Boolean(default=True,string="Description")
	print_box_per_row = fields.Selection(
		[('two_box_per_row', '2 box per row'),
		('three_box_per_row', '3 box per row'),
		('four_box_per_row', '4 box per row')],
		string='Print box per row',
		default='two_box_per_row')



	@api.onchange('catalog_type')
	def _onchange_catalog_type(self):
		if self.catalog_type == 'product':
			self.categories_ids = False
		else:
			self.product_ids = False


	def print_style_catalog(self):
		Attachments = self.env['ir.attachment']
		product_catalog_obj = self.env['product.catalog.generator']
		if self.report_style == 'style_1':
			[data] = self.read()
			datas = {
				 'ids': [1],
				 'model': 'product.catalog',
				 'form': data
			}
			action = self.env.ref('product_catalog_generator_app.action_report_product_catalog_style_1').\
				report_action(self, data=datas)
			action.update({'close_on_report_download': True})
			product_catalog_id = product_catalog_obj.create({
				'create_date': fields.Datetime.now()
			})
			product_catalog_pdf = self.env.ref('product_catalog_generator_app.action_report_product_catalog_style_1')._render_qweb_pdf(product_catalog_id.id,data=datas)[0]
			Attachments.sudo().create({
				'name': 'Product Catalog Report Style 1.pdf',
				'datas': base64.b64encode(product_catalog_pdf),
				'res_model': 'product.catalog.generator',
				'res_id': product_catalog_id.id,
				'mimetype': 'application/pdf',
				'type': 'binary',
			}) 
			return action

		elif self.report_style == 'style_2':
			[data] = self.read()
			datas = {
				 'ids': [1],
				 'model': 'product.catalog',
				 'form': data
			}
			action = self.env.ref('product_catalog_generator_app.action_report_product_catalog_style_2').\
				report_action(self, data=datas)
			action.update({'close_on_report_download': True})
			product_catalog_id = product_catalog_obj.create({
				'create_date': fields.Datetime.now()
			})
			product_catalog_pdf = self.env.ref('product_catalog_generator_app.action_report_product_catalog_style_2')._render_qweb_pdf(product_catalog_id.id,data=datas)[0]
			Attachments.sudo().create({
				'name': 'Product Catalog Report Style 2.pdf',
				'datas': base64.b64encode(product_catalog_pdf),
				'res_model': 'product.catalog.generator',
				'res_id': product_catalog_id.id,
				'mimetype': 'application/pdf',
				'type': 'binary',
			})
			return action

		elif self.report_style == 'style_3':
			[data] = self.read()
			datas = {
				 'ids': [1],
				 'model': 'product.catalog',
				 'form': data
			}
			action = self.env.ref('product_catalog_generator_app.action_report_product_catalog_style_3').\
				report_action(self, data=datas)
			action.update({'close_on_report_download': True})
			product_catalog_id = product_catalog_obj.create({
				'create_date': fields.Datetime.now()
			})
			product_catalog_pdf = self.env.ref('product_catalog_generator_app.action_report_product_catalog_style_3')._render_qweb_pdf(product_catalog_id.id,data=datas)[0]
			Attachments.sudo().create({
				'name': 'Product Catalog Report Style 3.pdf',
				'datas': base64.b64encode(product_catalog_pdf),
				'res_model': 'product.catalog.generator',
				'res_id': product_catalog_id.id,
				'mimetype': 'application/pdf',
				'type': 'binary',
			})
			return action

		elif self.report_style == 'style_4':
			[data] = self.read()
			datas = {
				 'ids': [1],
				 'model': 'product.catalog',
				 'form': data
			}
			action = self.env.ref('product_catalog_generator_app.action_report_product_catalog_style_4').\
				report_action(self, data=datas)
			action.update({'close_on_report_download': True})
			product_catalog_id = product_catalog_obj.create({
				'create_date': fields.Datetime.now()
			})
			product_catalog_pdf = self.env.ref('product_catalog_generator_app.action_report_product_catalog_style_4')._render_qweb_pdf(product_catalog_id.id,data=datas)[0]
			Attachments.sudo().create({
				'name': 'Product Catalog Report Style 4.pdf',
				'datas': base64.b64encode(product_catalog_pdf),
				'res_model': 'product.catalog.generator',
				'res_id': product_catalog_id.id,
				'mimetype': 'application/pdf',
				'type': 'binary',
			})
			return action

		elif self.report_style == 'style_5':
			[data] = self.read()
			datas = {
				 'ids': [1],
				 'model': 'product.catalog',
				 'form': data
			}
			action = self.env.ref('product_catalog_generator_app.action_report_product_catalog_style_5').\
				report_action(self, data=datas)
			action.update({'close_on_report_download': True})
			product_catalog_id = product_catalog_obj.create({
				'create_date': fields.Datetime.now()
			})
			product_catalog_pdf = self.env.ref('product_catalog_generator_app.action_report_product_catalog_style_5')._render_qweb_pdf(product_catalog_id.id,data=datas)[0]
			Attachments.sudo().create({
				'name': 'Product Catalog Report Style 5.pdf',
				'datas': base64.b64encode(product_catalog_pdf),
				'res_model': 'product.catalog.generator',
				'res_id': product_catalog_id.id,
				'mimetype': 'application/pdf',
				'type': 'binary',
			})
			return action

