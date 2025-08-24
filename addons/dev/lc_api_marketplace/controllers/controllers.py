# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class LcApiMarketplace(http.Controller):

    @http.route('/api/product/', website=True, auth='public')
    def product_template_list(self, **kw):
        product = request.env['product.template'].sudo().search([])        
        return request.render('lc_api_marketplace.product_page', {
            'template': product
        })
    
    @http.route('/api/get_product/', type='json', auth='user')
    def get_product_template(self):
        products_rec = request.env['product.template'].search([])
        products = []
        for rec in products_rec:
            vals = {
                'id': rec.id,
                'name': rec.name,
            }
            products.append(vals)
        data = {'status':200, 'response': products, 'message': 'Success'}
        return data