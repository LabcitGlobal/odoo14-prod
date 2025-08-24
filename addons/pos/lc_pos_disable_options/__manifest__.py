# -*- coding: utf-8 -*-
{
    'name': "Pos Disable Buttons",

    'summary': """
        Pos Disable Buttons""",

    'description': """
        Pos Disable Buttons
    """,

    'author': "Labcit Inc",
    'website': "http://www.labcit.com",
    'category': 'Point Of Sale',    
    'version': '14.0.1',
    'depends': ['point_of_sale'],    
    'data': [        
        'views/assets.xml',            
        'views/pos_disable_views.xml',
    ],
    'qweb': ['static/src/xml/pos_disabled.xml'],
    
    'installable': True,
    'application': True,
    'auto_install': False,
}