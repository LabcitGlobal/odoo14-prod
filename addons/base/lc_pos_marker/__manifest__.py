# -*- coding: utf-8 -*-
{
    'name': "Marcar puntos de entrega",

    'summary': """
        Modulo para Marcar puntos de entrega por Fecha""",

    'description': """
        Modulo para Marcar puntos de entrega por Fecha
    """,

    'author': "Labcit Inc.",
    'website': "http://www.labcit.com",
    
    'category': 'Manufacturing',
    'version': '14.0.1',

    # any module necessary for this one to work correctly
    'depends': ['point_of_sale','hr'],

    # always loaded
    'data': [                               
        'security/ir.model.access.csv',
        'wizards/pos_marker_view.xml',                
    ], 
    'installable': True,
    'application': True,  
}