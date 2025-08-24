from odoo import http
from odoo.http import request

class Main(http.Controller):
 
    @http.route('/services', type='http', auth="public", website=True)
    def lcsupport_services(self, **post):
        if post.get('case_number'):
            case_number = int(post.get('case_number'))
            return request.redirect('/services/%s' % case_number)
        else:
            return request.redirect('/')
        
    @http.route('/services/<int:case_number>', type="http", auth="public", website=True)
    def lcsupport_service_detail(self, case_number, **post):        
        return request.render('lcsupport_tracking.service_detail', {
            'service': request.env['lcsupport.service'].sudo().search([('id','=',case_number)]),            
            'submitted': post.get('submitted', False)
        })
