# -*- coding: utf-8 -*-
{
    'name': "Lc Web Frontend",

    'summary': """
        Modulo corregir el Menu Categorias y ocultar la cantidad en Website""",

    'description': """
        Modulo corregir el Menu Categorias y ocultar la cantidad en Website.
    """,

    'author': "Labcit Inc.",
    'website': "http://www.labcit.com",
    
    'category': 'Web',
    'version': '14.0.1',

    # any module necessary for this one to work correctly
    'depends': ['website'],

    # always loaded
    'data': [        
        'views/frontend_template.xml',       
    ], 
    'installable': True,
    'application': True,  
}