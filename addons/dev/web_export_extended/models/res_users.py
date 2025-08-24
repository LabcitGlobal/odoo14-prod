from odoo import api, fields, models


class res_groups(models.Model):
    
    _inherit = "res.users"

    # @api.model
    def export_check_credentials(self, password):
        print("+++++++++++++password++++++",password)
        env = {'interactive':True}
        try:

            self._check_credentials(password,env)


            return True
        except:
            return False
