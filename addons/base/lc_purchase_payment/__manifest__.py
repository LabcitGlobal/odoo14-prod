# -*- coding: utf-8 -*-
{
    'name': "Expand Payment Purchase",

    'summary': """
        Add column payment in Purchase Order.""",

    'description': """
        Add column field payment for module lccash in Purchase Order.
    """,

    'author': "Labcit Inc.",
    'website': "http://www.labcit.com",
    
    'category': 'Purchase',
    'version': '14.0.1',

    # any module necessary for this one to work correctly
    'depends': ['purchase','lccash'],

    # always loaded
    'data': [                       
        'views/views.xml',
    ], 
    'installable': True,
    'application': True,  
}