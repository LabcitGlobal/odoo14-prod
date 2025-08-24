# -*- coding: utf-8 -*-
# from odoo import http


# class LcFleetService(http.Controller):
#     @http.route('/lc_fleet_service/lc_fleet_service/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/lc_fleet_service/lc_fleet_service/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('lc_fleet_service.listing', {
#             'root': '/lc_fleet_service/lc_fleet_service',
#             'objects': http.request.env['lc_fleet_service.lc_fleet_service'].search([]),
#         })

#     @http.route('/lc_fleet_service/lc_fleet_service/objects/<model("lc_fleet_service.lc_fleet_service"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('lc_fleet_service.object', {
#             'object': obj
#         })
