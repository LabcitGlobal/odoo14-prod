# -*- coding: utf-8 -*-
{
    'name': "Expand Payment POS",

    'summary': """
        Add column payment in POS.""",

    'description': """
        Add column field payment for module lccash in POS.
    """,

    'author': "Labcit Inc.",
    'website': "http://www.labcit.com",
    
    'category': 'Point of Sale',
    'version': '14.0.1',

    # any module necessary for this one to work correctly
    'depends': ['point_of_sale','lccash'],

    # always loaded
    'data': [                       
        'views/views.xml',
    ], 
    'installable': True,
    'application': True,  
}