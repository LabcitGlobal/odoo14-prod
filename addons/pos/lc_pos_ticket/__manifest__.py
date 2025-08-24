# -*- coding: utf-8 -*-
{
    'name': "Formato Impresion POS 1/2 Carta",

    'summary': """
        Formato de impresion para hoja media carta""",

    'description': """
        Formato de impresion para hoja media carta
    """,

    'author': "Labcit Inc.",
    'website': "http://www.labcit.com",        
    'category': 'Point of Sale',
    'version': '14.0.1',

    'depends': ['point_of_sale'],
    
    'data': [        
        'views/views.xml',        
    ],
    'qweb': ['static/src/xml/lc_pos_ticket_view.xml'],
    'installable': True,
    'application': True,
    'auto_install': False,
}