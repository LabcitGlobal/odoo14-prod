# -*- coding: utf-8 -*-
#############################################################################
#
#    Copyright (C) 2021-TODAY Labcit Co(<https://www.labcit.com>)
#    Author: Labcit (<https://www.labcit.com>)
#
#############################################################################

from odoo import models


class ThemeLabcit(models.AbstractModel):
    _inherit = 'theme.utils'
    
    def _theme_labcit_post_copy(self, mod):
        
        self.disable_view('website.template_header_default')
        self.enable_view('theme_labcit.labcit_header')

        # self.disable_view('website.footer_custom')
        # self.enable_view('theme_labcit.labcit_footer')