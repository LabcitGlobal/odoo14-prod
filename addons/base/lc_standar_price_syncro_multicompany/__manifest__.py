# -*- coding: utf-8 -*-
{
    'name': "Synchronization of product prices in multicompany",

    'summary': """
        synchronization of product prices in multicompany, set the default cost to null, so that the cost is replicated to other companies.""",

    'description': """
        synchronization of product prices in multicompany, set the default cost to null, so that the cost is replicated to other companies.
    """,

    'author': "Labcit Inc.",
    'website': "http://www.labcit.com",        
    'category': 'Account',
    'version': '14.0.1',

    'depends': ['stock','hide_cost_price'],
    
    'data': [        
        # 'security/ir.model.access.csv',                        
        'views/product_template_views.xml',        
    ],     
    'installable': True,
    'application': True,
    'auto_install': False,
}