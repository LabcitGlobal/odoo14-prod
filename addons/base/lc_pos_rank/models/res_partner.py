# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date
from pytz import timezone

class LcPartnerPosOrders(models.TransientModel):
    _name = 'lc.partner.pos.orders'    

    from_date = fields.Date('From Date', default=lambda self:fields.Date.to_string(date.today()),required=True)
    to_date = fields.Date('To Date', default=lambda self: fields.Date.to_string(date.today()), required=True)    


    def set_pos_partner_rank(self):
        self.reset_pos_partner_rank()
        sql_query = """
            UPDATE res_partner SET number_pos_rank=rank, orders_pos_rank=t.total_orders, amount_pos_rank=t.total_mount, margin_pos_rank=t.total_margin
            FROM (SELECT 	
            	partner_id, 
            	nextval('pos_order_rank') AS rank, 
                COUNT(*) AS total_orders, 
                ROUND(SUM(amount_total),2) AS total_mount, 
                ROUND(SUM(margin),2) AS total_margin
            FROM pos_order 
            WHERE DATE(date_order::timestamp at time zone 'UTC') BETWEEN '%s' AND '%s'
            GROUP BY partner_id
            ORDER BY total_margin desc) AS t
            WHERE res_partner.id=t.partner_id;
            """ % (self.from_date,self.to_date)
        self.env.cr.execute(sql_query)

    # def set_pos_partner_rank(self):
    #     partners = self.env['res.partner'].search([])
    #     partner_rank_list = []
    #     for partner in partners:
    #         if partner.id:                
    #             total_margin = 0
    #             total_amount = 0
    #             total_orders = 0
    #             pos_orders = self.env['pos.order'].search([('partner_id','=',partner.id)])
    #             if pos_orders:
    #                 for order in pos_orders:
    #                     total_margin = total_margin + order.margin
    #                     total_orders = total_orders + 1
    #                     total_amount = total_amount + order.amount_total
    #                 partner_dict = { 'partner' : partner, 'total_margin' : total_margin, 'total_amount' : total_amount, 'total_orders' : total_orders}
    #                 partner_rank_list.append(partner_dict)

    #             if partner_rank_list:
    #                 newlist = sorted(partner_rank_list, key=lambda k: k.get('total_margin'), reverse=True)
    #                 rank = 0
    #                 for line in newlist:
    #                     if line:
    #                         rank = rank + 1
    #                         line['partner'].write({'number_pos_rank' : rank})
    #                         line['partner'].write({'orders_pos_rank' : line['total_orders']})
    #                         line['partner'].write({'amount_pos_rank' : line['total_amount']})
    #                         line['partner'].write({'margin_pos_rank' : line['total_margin']})
        
    def reset_pos_partner_rank(self):
        sql_query = """
        CREATE SEQUENCE IF NOT EXISTS pos_order_rank INCREMENT 1 START 1;
        ALTER SEQUENCE pos_order_rank RESTART;
        UPDATE res_partner SET number_pos_rank=0, orders_pos_rank=0, amount_pos_rank=0, margin_pos_rank=0;
        """
        self.env.cr.execute(sql_query)

class RankPartner(models.Model):
    _inherit = "res.partner"

    number_pos_rank = fields.Integer(string="Rank")        
    orders_pos_rank = fields.Float(string="Total")
    amount_pos_rank = fields.Float(string="Amount")
    margin_pos_rank = fields.Float(string="Margin")
    awards_count = fields.Integer(string="Awards", compute='get_awards_count')        

    def get_awards_count(self):
        count = self.env['lc.partner.awards'].search_count([('name','=',self.id)])
        self.awards_count = count

    def open_awards(self):
        return {
            'name': 'Awards',
            'domain': [('name','=',self.id)],            
            'res_model': 'lc.partner.awards',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }