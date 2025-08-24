# -*- coding: utf-8 -*-

from odoo import http

class LandingWebsite(http.Controller):
    @http.route('/landingpage', auth='public', website=True)
    def index(self, **kw):
        return http.request.render('theme_labcit.landingpage', {})