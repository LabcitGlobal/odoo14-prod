# -*- coding: utf-8 -*-
{
    'name': "View Stock Quant for Multicompany",

    'summary': """
        View Stock Quant for Multicompany""",

    'description': """
        View Stock Quant for Multicompany
    """,

    'author': "Labcit Inc",
    'website': "http://www.labcit.com",
    'category': 'Point Of Sale',    
    'version': '14.0.0.1',
    'depends': ['stock'],    
    'data': [        
        "security/ir.model.access.csv",
        "security/stock_quant_security.xml",
        "views/product_template_views.xml",        
        "views/view_stock_quant_multicompany.xml",        
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}