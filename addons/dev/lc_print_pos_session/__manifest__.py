# -*- coding: utf-8 -*-
{
    'name': "Impresion de Hoja de Ruta por Session",
    'version': "14.0.0",
    'summary': "",
    'category': 'Point Of Sale',
    "license": "AGPL-3",
    'description': """
    """,
    'author': "Labcit",
    'depends': ['point_of_sale'],
    'data': [
        'reports/pos_report.xml',
        'reports/pos_session_hoja_ruta.xml',
        'reports/pos_session_report_template.xml'
    ],    
    'installable': True,
    'application': False,
    'auto_install': False,
}