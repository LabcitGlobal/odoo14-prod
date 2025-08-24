# -*- coding: utf-8 -*-
{
    'name': "Module Delivery",

    'summary': """
        Module Delivery, admin agent, cost, margin.""",

    'description': """
        Module Delivery, admin agent, cost, margin.
    """,

    'author': "Labcit Inc.",
    'website': "http://www.labcit.com",
    
    'category': 'Sales',
    'version': '14.0.1',

    # any module necessary for this one to work correctly
    'depends': ['contacts'],

    # always loaded
    'data': [        
        'security/ir.model.access.csv',
        'views/delivery_cost_views.xml',        
        'views/partner_kanban_view.xml',        
    ], 
    'installable': True,
    'application': True,  
}