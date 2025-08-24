from odoo import models, fields, api, _


class StockQuantProductTemplate(models.Model):
    _inherit = 'product.template'

    def stock_quant_product_template(self):
        return {'type': 'ir.actions.act_window',
                'name': _('Stock Quant for Multicompany'),
                'domain': [('product_tmpl_id','=',self.id)],
                'res_model': 'view.stock.quant.multicompany',
                'view_id': False,
                'view_mode': 'tree',
                }
