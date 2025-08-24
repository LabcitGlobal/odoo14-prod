# -*- coding: utf-8 -*-
{
    'name': "Add fields in contact module in the list view",

    'summary': """
        Add fields in contact module in the list view (Mobile, Pricelist)""",

    'description': """
        Add fields in contact module in the list view (Mobile, Pricelist).
    """,

    'author': "Labcit Inc.",
    'website': "http://www.labcit.com",
    
    'category': 'Sales/CRM',
    'version': '14.0.1',

    # any module necessary for this one to work correctly
    'depends': ['contacts'],

    # always loaded
    'data': [        
        'views/contact_view.xml',        
    ], 
    'installable': True,
    'application': True,  
}