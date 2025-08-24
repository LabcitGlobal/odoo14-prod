# -*- coding: utf-8 -*-

from odoo import models, fields, api

class LcSessionMarker(models.Model):
    _inherit = 'pos.session'    

    def make_pos_session(self):
        sql_query = """
        update res_partner set marker_color='green' where marker_color!='green' and marker_color!='orange';        

        update res_partner set marker_color='red' where id in(
        SELECT DISTINCT partner_id
        FROM pos_order o,  
        (select DATE(start_at::timestamp at time zone 'UTC') as dates, user_id from pos_session where id=%s) s
        WHERE DATE(o.date_order::timestamp at time zone 'UTC') = s.dates 
        AND partner_id IS NOT NULL 
        AND o.user_id in(select name from lccommission_agent) 
        AND o.amount_total>0 
        AND o.name NOT IN(SELECT * FROM lc_posorderrefund_view)
        );
        """ % (self.id)
        self.env.cr.execute(sql_query)