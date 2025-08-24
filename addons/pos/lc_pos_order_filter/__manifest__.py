# -*- coding: utf-8 -*-
{
    'name': "Filter Pos Order 3 months",

    'summary': """
        Module for Filter Pos Order 3 months""",

    'description': """
        Module for Filter Pos Order 3 months
    """,

    'author': "Labcit Inc.",
    'website': "http://www.labcit.com",
    
    'category': 'Manufacturing',
    'version': '14.0.1',

    # any module necessary for this one to work correctly
    'depends': ['point_of_sale'],

    # always loaded
    'data': [                               
        'views/filter_order_views.xml',                
    ], 
    'installable': True,
    'application': True,  
}