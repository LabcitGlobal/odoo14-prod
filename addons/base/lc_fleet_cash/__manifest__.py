# -*- coding: utf-8 -*-
{
    'name': "Add Fleet Service into module Payment",

    'summary': """
        Add Field Fleet Service into module Lc Cash""",

    'description': """
        Add Field Fleet Service into module Lc Cash.
    """,

    'author': "Labcit Inc.",
    'website': "http://www.labcit.com",
    
    'category': 'Manufacturing',
    'version': '14.0.1',

    # any module necessary for this one to work correctly
    'depends': ['lccash','lc_fleet_service'],

    # always loaded
    'data': [        
        'views/payment_fleet_service.xml',        
        'reports/menu_config_report.xml',        
        'reports/payment_fleet_service_report.xml',        
    ], 
    'installable': True,
    'application': True,  
}