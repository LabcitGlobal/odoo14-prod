# -*- coding: utf-8 -*-

from odoo import models, fields, api
from mako.runtime import _inherit_from

class lc_attendance_comment(models.Model):        
    _inherit = 'hr.attendance'

    comment = fields.Char(string='Comentario')