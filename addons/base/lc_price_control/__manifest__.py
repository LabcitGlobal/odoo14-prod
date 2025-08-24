# -*- coding: utf-8 -*-
{
    'name': "Verification of errors in prices",

    'summary': """
        Verification of errors in prices""",

    'description': """
        Verification of errors in prices
    """,

    'author': "Labcit Inc.",
    'website': "http://www.labcit.com",
    
    'category': 'Manufacturing',
    'version': '14.0.1',

    # any module necessary for this one to work correctly
    'depends': ['stock'],

    # always loaded
    'data': [        
        'security/ir.model.access.csv',        
        'views/product_price_control.xml',                
    ], 
    'installable': True,
    'application': True,  
}