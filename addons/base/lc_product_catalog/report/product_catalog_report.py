# -*- coding: utf-8 -*-


from datetime import datetime, timedelta
from odoo import models, api,fields
from odoo.tools import pycompat, DEFAULT_SERVER_DATETIME_FORMAT,DEFAULT_SERVER_DATE_FORMAT
from odoo.tools.float_utils import float_round


class LcProductCatalogReportStyle1(models.AbstractModel):
	_name = 'report.lc_product_catalog.report_product_style_1' 
	_description = 'Product Catalog Report Style'


	def _get_product_details(self, data):
		category_ids = data.get('category_ids')
		filter_type = data.get('filter_type')
		product_ids = data.get('product_ids')
		if filter_type == 'category':
			product_ids = self.env['product.product'].search([('categ_id', 'child_of', category_ids.ids)], order="categ_id asc, name asc")
		else:
			product_ids = self.env['product.product'].search([('id', 'in', product_ids.ids)], order="categ_id asc, name asc")
		return product_ids


	@api.model
	def _get_report_values(self, docids, data=None):
		filter_type = data['form']['catalog_type']
		category_ids = self.env['product.category'].browse(data['form']['categories_ids'])
		product_ids  = self.env['product.product'].browse(data['form']['product_ids'])
		if data['form'].get('currency_id'):
			currency_id = self.env['res.currency'].browse(data['form']['currency_id'][0])
		else:
			currency_id = False
		price_check = data['form']['price']
		image_size = data['form']['image_size']
		report_style = data['form']['report_style']
		description_check = data['form']['description']
		print_box_per_row = data['form']['print_box_per_row']
		category_check = data['form']['category_name']
		image_check = data['form']['image_check']
		quant_stock_check = data['form']['quant_stock_check']
		watermark_check = data['form']['pdf_watermark']
		data  = { 
			'filter_type'   : filter_type,
			'product_ids'   : product_ids,
			'category_ids'  : category_ids,
			'currency_id'  : currency_id,
			'price_check'  : price_check,
			'image_size'  : image_size,
			'report_style'  : report_style,
			'description_check'  : description_check,
			'print_box_per_row'  : print_box_per_row,
			'category_check'  : category_check,
			'image_check'  : image_check,
			'quant_stock_check'  : quant_stock_check,
			'watermark_check'  : watermark_check,
		} 
		docargs = {
				   'doc_model': 'lc.product.catalog',
				   'data': data,
				   'get_product_details':self._get_product_details,
				   }
		return docargs

class LcProductCatalogReportStyle2(models.AbstractModel):
	_name = 'report.lc_product_catalog.report_product_style_2' 
	_description = 'Product Catalog Report Style'


	def _get_product_details(self, data):
		category_ids = data.get('category_ids')
		filter_type = data.get('filter_type')
		product_ids = data.get('product_ids')
		if filter_type == 'category':
			product_ids = self.env['product.product'].search([('categ_id', 'child_of', category_ids.ids)], order="categ_id asc, name asc")
		else:
			product_ids = self.env['product.product'].search([('id', 'in', product_ids.ids)], order="categ_id asc, name asc")
		return product_ids

	@api.model
	def _get_report_values(self, docids, data=None):
		filter_type = data['form']['catalog_type']
		category_ids = self.env['product.category'].browse(data['form']['categories_ids'])
		product_ids  = self.env['product.product'].browse(data['form']['product_ids'])
		if data['form'].get('currency_id'):
			currency_id = self.env['res.currency'].browse(data['form']['currency_id'][0])
		else:
			currency_id = False
		price_check = data['form']['price']
		image_size = data['form']['image_size']
		report_style = data['form']['report_style']
		description_check = data['form']['description']
		print_box_per_row = data['form']['print_box_per_row']
		category_check = data['form']['category_name']
		quant_stock_check = data['form']['quant_stock_check']
		data  = { 
			'filter_type'   : filter_type,
			'product_ids'   : product_ids,
			'category_ids'  : category_ids,
			'currency_id'  : currency_id,
			'price_check'  : price_check,
			'image_size'  : image_size,
			'report_style'  : report_style,
			'description_check'  : description_check,
			'print_box_per_row'  : print_box_per_row,
			'category_check'  : category_check,
			'quant_stock_check'  : quant_stock_check,
		} 
		docargs = {
				   'doc_model': 'lc.product.catalog',
				   'data': data,
				   'get_product_details':self._get_product_details,
				   }
		return docargs


class LcProductCatalogReportStyle3(models.AbstractModel):
	_name = 'report.lc_product_catalog.report_product_style_3' 
	_description = 'Product Catalog Report Style'


	def _get_product_details(self, data):
		category_ids = data.get('category_ids')
		filter_type = data.get('filter_type')
		product_ids = data.get('product_ids')
		if filter_type == 'category':
			product_ids = self.env['product.product'].search([('categ_id', 'child_of', category_ids.ids)], order="categ_id asc, name asc")
		else:
			product_ids = self.env['product.product'].search([('id', 'in', product_ids.ids)], order="categ_id asc, name asc")
		return product_ids


	@api.model
	def _get_report_values(self, docids, data=None):
		filter_type = data['form']['catalog_type']
		category_ids = self.env['product.category'].browse(data['form']['categories_ids'])
		product_ids  = self.env['product.product'].browse(data['form']['product_ids'])
		if data['form'].get('currency_id'):
			currency_id = self.env['res.currency'].browse(data['form']['currency_id'][0])
		else:
			currency_id = False
		price_check = data['form']['price']
		image_size = data['form']['image_size']
		report_style = data['form']['report_style']
		description_check = data['form']['description']
		print_box_per_row = data['form']['print_box_per_row']
		quant_stock_check = data['form']['quant_stock_check']
		category_check = data['form']['category_name']
		data  = { 
			'filter_type'   : filter_type,
			'product_ids'   : product_ids,
			'category_ids'  : category_ids,
			'currency_id'  : currency_id,
			'price_check'  : price_check,
			'image_size'  : image_size,
			'report_style'  : report_style,
			'description_check'  : description_check,
			'print_box_per_row'  : print_box_per_row,
			'quant_stock_check'  : quant_stock_check,
			'category_check'  : category_check,
		} 
		docargs = {
				   'doc_model': 'lc.product.catalog',
				   'data': data,
				   'get_product_details':self._get_product_details,
				   }
		return docargs


class LcProductCatalogReportStyle4(models.AbstractModel):
	_name = 'report.lc_product_catalog.report_product_style_4' 
	_description = 'Product Catalog Report Style'


	def _get_product_details(self, data):
		category_ids = data.get('category_ids')
		filter_type = data.get('filter_type')
		product_ids = data.get('product_ids')
		if filter_type == 'category':
			product_ids = self.env['product.product'].search([('categ_id', 'child_of', category_ids.ids)], order="categ_id asc, name asc")
		else:
			product_ids = self.env['product.product'].search([('id', 'in', product_ids.ids)], order="categ_id asc, name asc")
		return product_ids


	@api.model
	def _get_report_values(self, docids, data=None):
		filter_type = data['form']['catalog_type']
		category_ids = self.env['product.category'].browse(data['form']['categories_ids'])
		product_ids  = self.env['product.product'].browse(data['form']['product_ids'])
		if data['form'].get('currency_id'):
			currency_id = self.env['res.currency'].browse(data['form']['currency_id'][0])
		else:
			currency_id = False
		price_check = data['form']['price']
		image_size = data['form']['image_size']
		report_style = data['form']['report_style']
		description_check = data['form']['description']
		print_box_per_row = data['form']['print_box_per_row']
		quant_stock_check = data['form']['quant_stock_check']
		category_check = data['form']['category_name']
		data  = { 
			'filter_type'   : filter_type,
			'product_ids'   : product_ids,
			'category_ids'  : category_ids,
			'currency_id'  : currency_id,
			'price_check'  : price_check,
			'image_size'  : image_size,
			'report_style'  : report_style,
			'description_check'  : description_check,
			'print_box_per_row'  : print_box_per_row,
			'quant_stock_check'  : quant_stock_check,
			'category_check'  : category_check,
		} 
		docargs = {
				   'doc_model': 'lc.product.catalog',
				   'data': data,
				   'get_product_details':self._get_product_details,
				   }
		return docargs


class LcProductCatalogReportStyle5(models.AbstractModel):
	_name = 'report.lc_product_catalog.report_product_style_5' 
	_description = 'Product Catalog Report Style'


	def _get_product_details(self, data):
		category_ids = data.get('category_ids')
		filter_type = data.get('filter_type')
		product_ids = data.get('product_ids')
		if filter_type == 'category':
			product_ids = self.env['product.product'].search([('categ_id', 'child_of', category_ids.ids)], order="categ_id asc, name asc")
		else:
			product_ids = self.env['product.product'].search([('id', 'in', product_ids.ids)], order="categ_id asc, name asc")
		return product_ids


	@api.model
	def _get_report_values(self, docids, data=None):
		filter_type = data['form']['catalog_type']
		category_ids = self.env['product.category'].browse(data['form']['categories_ids'])
		product_ids  = self.env['product.product'].browse(data['form']['product_ids'])
		if data['form'].get('currency_id'):
			currency_id = self.env['res.currency'].browse(data['form']['currency_id'][0])
		else:
			currency_id = False
		price_check = data['form']['price']
		image_size = data['form']['image_size']
		report_style = data['form']['report_style']
		description_check = data['form']['description']
		print_box_per_row = data['form']['print_box_per_row']
		quant_stock_check = data['form']['quant_stock_check']
		category_check = data['form']['category_name']
		data  = { 
			'filter_type'   : filter_type,
			'product_ids'   : product_ids,
			'category_ids'  : category_ids,
			'currency_id'  : currency_id,
			'price_check'  : price_check,
			'image_size'  : image_size,
			'report_style'  : report_style,
			'description_check'  : description_check,
			'print_box_per_row'  : print_box_per_row,
			'quant_stock_check'  : quant_stock_check,
			'category_check'  : category_check,
		} 
		docargs = {
				   'doc_model': 'lc.product.catalog',
				   'data': data,
				   'get_product_details':self._get_product_details,
				   }
		return docargs
	
class LcProductCatalogReportStyle6(models.AbstractModel):
	_name = 'report.lc_product_catalog.report_product_style_6' 
	_description = 'Product Catalog Report Style'


	def _get_product_details(self, data):
		category_ids = data.get('category_ids')
		filter_type = data.get('filter_type')
		product_ids = data.get('product_ids')
		if filter_type == 'category':
			product_ids = self.env['product.product'].search([('categ_id', 'child_of', category_ids.ids)], order="categ_id asc, name asc")
		else:
			product_ids = self.env['product.product'].search([('id', 'in', product_ids.ids)], order="categ_id asc, name asc")
		return product_ids


	@api.model
	def _get_report_values(self, docids, data=None):
		filter_type = data['form']['catalog_type']
		category_ids = self.env['product.category'].browse(data['form']['categories_ids'])
		product_ids  = self.env['product.product'].browse(data['form']['product_ids'])
		if data['form'].get('currency_id'):
			currency_id = self.env['res.currency'].browse(data['form']['currency_id'][0])
		else:
			currency_id = False
		price_check = data['form']['price']
		image_size = data['form']['image_size']
		report_style = data['form']['report_style']
		description_check = data['form']['description']
		print_box_per_row = data['form']['print_box_per_row']
		category_check = data['form']['category_name']
		image_check = data['form']['image_check']
		quant_stock_check = data['form']['quant_stock_check']
		watermark_check = data['form']['pdf_watermark']
		data  = { 
			'filter_type'   : filter_type,
			'product_ids'   : product_ids,
			'category_ids'  : category_ids,
			'currency_id'  : currency_id,
			'price_check'  : price_check,
			'image_size'  : image_size,
			'report_style'  : report_style,
			'description_check'  : description_check,
			'print_box_per_row'  : print_box_per_row,
			'category_check'  : category_check,
			'image_check'  : image_check,
			'quant_stock_check'  : quant_stock_check,
			'watermark_check'  : watermark_check,
		} 
		docargs = {
				   'doc_model': 'lc.product.catalog',
				   'data': data,
				   'get_product_details':self._get_product_details,
				   }
		return docargs