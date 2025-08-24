# -*- coding: utf-8 -*-
{
    'name': "Purchase Commission",

    'summary': """
        Add fields to calculate the commission percentage of the order.""",

    'description': """
        Add fields to calculate the commission percentage of the order.
    """,

    'author': "Labcit Inc.",
    'website': "http://www.labcit.com",
    
    'category': 'Purchase',
    'version': '14.0.1',

    # any module necessary for this one to work correctly
    'depends': ['purchase'],

    # always loaded
    'data': [                       
        'views/views.xml',
    ], 
    'installable': True,
    'application': True,  
}