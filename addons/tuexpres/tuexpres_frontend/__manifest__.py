# -*- coding: utf-8 -*-
{
    'name': "Tuexpres Web Frontend",

    'summary': """
        Tuexpres Web Frontend""",

    'description': """
        Tuexpres Web Frontend.
    """,

    'author': "Labcit Inc.",
    'website': "http://www.labcit.com",
    
    'category': 'Web',
    'version': '14.0.1',

    # any module necessary for this one to work correctly
    'depends': ['website'],

    # always loaded
    'data': [        
        'views/frontend_template.xml',
        'views/product_pricelist_item.xml',
        'templates/product.xml',
        'templates/quick_view.xml',
        'templates/ajax_cart.xml',
    ], 
    'installable': True,
    'application': True,  
}