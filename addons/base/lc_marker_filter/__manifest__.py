# -*- coding: utf-8 -*-
{
    'name': "Filtro para Marcador",

    'summary': """
        Filtro para Marcador""",

    'description': """
        Filtro para Marcador
    """,

    'author': "Labcit Inc",
    'website': "http://www.labcit.com",
    'category': 'Point Of Sale',    
    'version': '14.0.0.1',
    'depends': ['base', 'account'],    
    'data': [
        "views/marker_filter.xml",        
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}