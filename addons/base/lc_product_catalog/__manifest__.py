# -*- coding: utf-8 -*-
{
    'name': "Lc Product Catalog",

    'summary': """
        Product catalog generator in pdf""",

    'description': """
        Product catalog generator in pdf.
    """,

    'author': "Labcit Inc.",
    'website': "http://www.labcit.com",
    
    'category': 'Sales',
    'version': '14.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale_management','account','stock'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',        
        'wizard/wizard_catalog_generator_views.xml',
        'report/product_catalog_report.xml',
        'report/product_catalog_report_views.xml',
    ], 
    'installable': True,
    'application': True,  
}