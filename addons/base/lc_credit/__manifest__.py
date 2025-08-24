# -*- coding: utf-8 -*-
{
    'name': "Pos Order Pending Payment",

    'summary': """
        Modulo para administrar Boletas pendientes del POS""",

    'description': """
        Modulo para administrar Boletas pendientes del POS.
    """,

    'author': "Labcit Inc.",
    'website': "http://www.labcit.com",
    
    'category': 'Manufacturing',
    'version': '14.0.1',

    # any module necessary for this one to work correctly
    'depends': ['point_of_sale','lccash'],

    # always loaded
    'data': [
        'security/groups.xml', 
        'security/ir.model.access.csv',        
        'views/lc_credit_partner.xml',
        'views/lc_credit_pos.xml',
    ], 
    'installable': True,
    'application': True,  
}