# -*- coding: utf-8 -*-
{
    'name': "Calculate the supplier's commission",

    'summary': """
        Calculate the supplier's commission""",

    'description': """
        Calculate the supplier's commission        
    """,

    'author': "Labcit Inc.",
    'website': "http://www.labcit.com",        
    'category': 'Sale',
    'version': '14.0.0',

    'depends': ['stock'],
    
    'data': [     
        'security/ir.model.access.csv',   
        'views/product_template_views.xml',        
    ],
    'installable': True,
    'application': True,
    'auto_install': False,    
}