# -*- coding: utf-8 -*-
{
    'name': "Update Purchase Order Line Prices",

    'summary': """
        Add column Cost from Purchase Order Line by Last Cost for Product""",

    'description': """
        Add column Cost from Purchase Order Line by Last Cost for Product.
    """,

    'author': "Ivan Carvajal Antiñapa",
    'website': "http://www.labcit.com",
    
    'category': 'Purchase',
    'version': '14.0.0',

    # any module necessary for this one to work correctly
    'depends': ['purchase'],

    # always loaded
    'data': [
          "views/purchase_orderprice.xml",       
        #   "views/assets.xml"
    ],
    # 'assets': {
    #     'web.assets_backend': [
    #         'lc_purchase_orderprice/static/src/css/styles.css',
    #     ],
    # }, 
    'installable': True,
    'application': True,  
}
