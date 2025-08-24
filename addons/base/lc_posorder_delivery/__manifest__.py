# -*- coding: utf-8 -*-
{
    'name': "Extendiendo el Modulo Pos Order para Envios",

    'summary': """
        Extendiendo el Modulo Pos Order para Envios""",

    'description': """
        Extendiendo el Modulo Pos Order para Envios
    """,

    'author': "Labcit Inc.",
    'website': "http://www.labcit.com",        
    'category': 'Account',
    'version': '14.0.1',

    'depends': ['point_of_sale','l10n_bo_country_state'],
    
    'data': [        
        'views/lc_pos_order.xml',
        'reports/lc_pos_print.xml', 
        'reports/pos_print_report_template.xml', 
    ],     
    'installable': True,
    'application': True,
    'auto_install': False,
}