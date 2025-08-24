# -*- coding: utf-8 -*-
{
    'name': "Add Agent into module Payment",

    'summary': """
        Add Field Commission Agent into module Lc Cash""",

    'description': """
        Add Field Commission Agent into module Lc Cash.
    """,

    'author': "Labcit Inc.",
    'website': "http://www.labcit.com",
    
    'category': 'Manufacturing',
    'version': '14.0.1',

    # any module necessary for this one to work correctly
    'depends': ['lccash','lccommission'],

    # always loaded
    'data': [        
        'views/lc_lccash_agent.xml',
        'views/lc_pos_order_agent.xml',        
    ], 
    'installable': True,
    'application': True,  
}