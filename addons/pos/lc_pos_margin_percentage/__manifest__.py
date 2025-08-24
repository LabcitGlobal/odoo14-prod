# -*- coding: utf-8 -*-
{
    'name': "lc_pos_margin_percentage",

    'summary': """
        Modulo para administrar el margen entre el precio de compra y el precio de venta por el POS""",

    'description': """
        Modulo para administrar el margen entre el precio de compra y el precio de venta por el POS
    """,

    'author': "Labcit Inc.",
    'website': "http://www.labcit.com",        
    'category': 'Tools',
    'version': '14.0.0',

    'depends': ['point_of_sale'],
    
    'data': [                
        'views/view_pos_order.xml',        
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}