# -*- coding: utf-8 -*-
{
    'name': "Fleet Services Tracking",

    'summary': """
        Module for fleet services tracking""",

    'description': """
        Module for fleet services tracking.
    """,

    'author': "Labcit Inc.",
    'website': "http://www.labcit.com",
    
    'category': 'Services',
    'version': '14.0.1',

    # any module necessary for this one to work correctly
    'depends': ['lc_fleet_service'],

    # always loaded
    'data': [
        # 'security/user_groups.xml', 
        # 'security/ir.model.access.csv',        
        'views/fleet_tracking_templates.xml',
        'views/snippets.xml',        
    ], 
    'installable': True,
    'application': True,  
}