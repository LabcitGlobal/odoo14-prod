# -*- coding: utf-8 -*-
{
    'name': "Services Tracking",

    'summary': """
        Service tracking""",

    'description': """
        Module for Service tracking.
    """,

    'author': "Labcit Inc.",
    'website': "http://www.labcit.com",
    
    'category': 'Services',
    'version': '14.0.1',

    # any module necessary for this one to work correctly
    'depends': ['lcsupport'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',        
        'views/lcsupport_tracking_views.xml',        
        'views/lcsupport_templates.xml',
        'views/snippets.xml',        
    ], 
    'installable': True,
    'application': True,  
}