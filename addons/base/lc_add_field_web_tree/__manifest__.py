# -*- coding: utf-8 -*-
{
    'name': "Add Fields Category in WEB list View",

    'summary': """
        Add Fields Category in WEB list View""",

    'description': """
        Add Fields Category in WEB list View.
    """,

    'author': "Labcit Inc.",
    'website': "http://www.labcit.com",
    
    'category': 'Website',
    'version': '14.0.1',

    # any module necessary for this one to work correctly
    'depends': ['website_sale'],

    # always loaded
    'data': [        
        'views/website_view.xml',        
    ], 
    'installable': True,
    'application': True,  
}