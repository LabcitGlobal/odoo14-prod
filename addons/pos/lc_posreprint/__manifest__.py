# -*- coding: utf-8 -*-
{
    'name': "lc_posreprint",

    'summary': """
        Modulo para reimprimir ordenes creadas en el Punto de Venta""",

    'description': """
        Modulo para reimprimir ordenes creadas en el Punto de Venta
    """,

    'author': "Labcit Inc",
    'website': "http://www.labcit.com",
    'category': 'Point Of Sale',    
    'version': '14.0.0',
    'depends': ['point_of_sale','aces_pos_note'],    
    'data': [        
        'views/views.xml',
        'reports/lc_pos_reprint.xml',
        'reports/pos_reprint_report_template.xml',        
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}