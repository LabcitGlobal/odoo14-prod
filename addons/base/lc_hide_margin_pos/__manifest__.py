# -*- coding: utf-8 -*-
{
    'name': "Ocultar Margen en POS",

    'summary': """
        Oculta el Margen en los modulos del Punto de Venta(POS)""",

    'description': """
        Oculta el Margen en los modulos del Punto de Venta(POS).
    """,

    'author': "Labcit Inc.",
    'website': "http://www.labcit.com",
    
    'category': 'Manufacturing',
    'version': '14.0.1',

    # any module necessary for this one to work correctly
    'depends': ['point_of_sale','sale','lc_pos_margin_percentage'],

    # always loaded
    'data': [
        'security/lc_hide_margin_pos.xml',
        'views/view_lc_hide_margin_pos.xml'         
    ], 
    'installable': True,
    'application': True,  
}