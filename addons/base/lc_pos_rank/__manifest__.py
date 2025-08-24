# -*- coding: utf-8 -*-
{
    'name': "Rank according to PTV orders",

    'summary': """
        Rank according to PTV orders""",

    'description': """
        Rank according to PTV orders
    """,

    'author': "Labcit Inc",
    'website': "http://www.labcit.com",
    'category': 'Point Of Sale',    
    'version': '14.0.0.1',
    'depends': ['point_of_sale'],    
    'data': [
        "security/ir.model.access.csv",
        # "security/user_security.xml",
        "wizards/res_partner_view.xml",        
        "views/partner_pos_view.xml",        
        "views/partner_kanban_view.xml",        
        "views/partner_awards_view.xml",        
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}