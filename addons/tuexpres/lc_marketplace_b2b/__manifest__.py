# -*- coding: utf-8 -*-
{
    'name': "Marketplace B2B",

    'summary': """
        Functions for Marketplace B2B.""",

    'description': """
        Functions for Marketplace B2B.
    """,

    'author': "Labcit Inc.",
    'website': "http://www.labcit.com",
    
    'category': 'Sales',
    'version': '14.0.1',

    # any module necessary for this one to work correctly
    'depends': ['contacts'],

    # always loaded
    'data': [
        'security/user_groups.xml',
        'security/ir.model.access.csv',
        # 'reports/config_consignment_report.xml',
        # 'reports/print_consignment_report_template.xml',
        'views/res_partner_view.xml',
        'views/product_template_view.xml',
        'views/marketplace_b2b_view.xml',
        'views/investment_pos_view.xml',
        'views/investment_product_view.xml',
    ], 
    'installable': True,
    'application': True,  
}