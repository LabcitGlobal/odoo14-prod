# -*- coding: utf-8 -*-
{
    'name': "Add Pos Category field in POS list View",

    'summary': """
        Add Pos Category field in POS list View""",

    'description': """
        Add Pos Category field in POS list View.
    """,

    'author': "Labcit Inc.",
    'website': "http://www.labcit.com",
    
    'category': 'Sales/Point of Sale',
    'version': '14.0.1',

    # any module necessary for this one to work correctly
    'depends': ['point_of_sale'],

    # always loaded
    'data': [        
        'views/point_of_sale_view.xml',        
    ], 
    'installable': True,
    'application': True,  
}