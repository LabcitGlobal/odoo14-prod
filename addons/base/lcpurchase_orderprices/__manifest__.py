# -*- coding: utf-8 -*-
{
    'name': "Update Purchase Order Line Prices",

    'summary': """
        Add column Cost from Purchase Order Line by Last Cost for Product""",

    'description': """
        Add column Cost from Purchase Order Line by Last Cost for Product.
    """,

    'author': "Labcit Inc.",
    'website': "http://www.labcit.com",
    
    'category': 'Purchase',
    'version': '14.0.1',

    # any module necessary for this one to work correctly
    'depends': ['purchase'],

    # always loaded
    'data': [
          "views/purchase_ordercost.xml",       
    ], 
    'installable': True,
    'application': True,  
}