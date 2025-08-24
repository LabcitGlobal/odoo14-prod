# -*- coding: utf-8 -*-
{
    'name': "Partner C.I. and District",

    'summary': """
        Add fields C.I. and District for plurinational state of Bolivia""",

    'description': """
        Add fields C.I. and District for plurinational state of Bolivia
        Issuing Department = La Paz
        Country = Bolivia
        Department = La Paz        
        City = El Alto        
    """,

    'author': "Labcit Inc.",
    'website': "http://www.labcit.com",        
    'category': 'Sale',
    'version': '14.0.0',

    'depends': ['contacts','l10n_bo_country_state'],
    
    'data': [        
        'views/views.xml',        
    ],
    'installable': True,
    'application': True,
    'auto_install': False,    
}