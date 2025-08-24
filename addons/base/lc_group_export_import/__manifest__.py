# -*- coding: utf-8 -*-
{
    'name': "Enable export/import for group",

    'summary': """
        Enable export/import for group""",

    'description': """
        Enable export/import for group.
    """,

    'author': "Labcit Inc.",
    'website': "http://www.labcit.com",
    
    'category': 'Web',
    'version': '14.0.1',

    # any module necessary for this one to work correctly
    'depends': ['web'],

    # always loaded
    'data': [
        'security/group_security.xml',
        'views/assets_view.xml',
    ], 
    'installable': True,
    'application': True,  
}