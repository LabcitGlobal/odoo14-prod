# -*- coding: utf-8 -*-
{
    'name': "Markar los puntos de la session",

    'summary': """
        Modulo para Markar los puntos de la session""",

    'description': """
        Modulo para Markar los puntos de la session.
    """,

    'author': "Labcit Inc.",
    'website': "http://www.labcit.com",
    
    'category': 'Manufacturing',
    'version': '14.0.1',

    # any module necessary for this one to work correctly
    'depends': ['point_of_sale'],

    # always loaded
    'data': [                       
        'views/view_pos_session.xml',        
    ], 
    'installable': True,
    'application': True,  
}