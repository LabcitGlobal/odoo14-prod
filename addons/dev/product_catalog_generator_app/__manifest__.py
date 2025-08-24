# -*- coding: utf-8 -*-

{
    'name' : 'Product Catalog Generator With Different Style App',
    'author': "Edge Technologies",
    'version' : '14.0.1.0',
    'live_test_url':'https://youtu.be/LlsxtWjeHTE',
    "images":['static/description/main_screenshot.png'],
    'summary' : 'Generate Product catalogue Product Catalog Generator generate Product Catalog with different style product different style catalog create product catalog add product catalog brand generate product catalogue generator design you own product catalog create',
    'description' : """ This module helps to provide a products Catalog with custom styles. This module can design a catalog with different styles like image size, boxes per row, show/hide descriptions, etc. Users can show  Created Catalog in Generated Catalog Menus.""",
    "license" : "OPL-1",
    'depends' : ['base','sale_management','account'],
    'data' : [
        'security/ir.model.access.csv',
        'data/sequence_data.xml',
        'data/mail_template_data.xml',
        'views/product_catalog_generator_view.xml',
        'wizard/product_catalog_generator_wizard_views.xml',
        'report/product_catalog_report.xml',
        'report/product_catalog_report_views.xml',
    ],
    'installable' : True,
    'auto_install' : False,
    'application': True,
    'price': 28,
    'currency': "EUR",
    'category' : 'Sales',
}
