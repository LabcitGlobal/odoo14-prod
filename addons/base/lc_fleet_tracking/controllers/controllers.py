from odoo import http
from odoo.http import request

class Main(http.Controller):
 
    @http.route('/rastreo', type='http', auth="public", website=True)
    def lc_fleet_services_tracking(self, **post):        
        if post.get('tracking_id'):
            tracking_id = post.get('tracking_id')
            if tracking_id.find('/') > 0:     
                return request.redirect('/rastreo/%s' % tracking_id.replace("/","_"))
            else:
                return request.redirect('/seguimiento?error=1')
        else:
            return request.redirect('/seguimiento?error=1')
        
    @http.route('/rastreo/<string:tracking_id>', type="http", auth="public", website=True)
    def lc_fleet_service_detail(self, tracking_id, **post):
        if tracking_id.find('_') > 0:            
            # service_id = int(tracking_id[tracking_id.find('/'):len(tracking_id)])
            service_id = tracking_id.replace("_","/")
            count_reg  = request.env['lc.fleet.tracking'].sudo().search_count([('service_id','=',service_id)])
            if count_reg > 0:
                return request.render('lc_fleet_tracking.fleet_service_detail', {
                    'tracking': request.env['lc.fleet.tracking'].sudo().search([('service_id','=',service_id)]),
                })
            else:
                return request.redirect('/seguimiento?error=1')
        else:
            return request.redirect('/seguimiento?error=1')

    @http.route('/seguimiento', type="http", auth="public", website=True)
    def lc_fleet_service_search(self, **post):
        if post.get('error'):
            error = post.get('error')
        else:
            error = 0
        return request.render('lc_fleet_tracking.fleet_service_search', {
            'error': error
        })