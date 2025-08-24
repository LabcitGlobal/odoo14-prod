# -*- coding: utf-8 -*-
{
    'name': "Print Pos Images Watermark",

    'summary': """
        print pos orders with images and watermark""",

    'description': """
        print pos orders with images and watermark.
    """,

    'author': "Labcit Inc.",
    'website': "http://www.labcit.com",
    
    'category': 'Manufacturing',
    'version': '14.0.1',

    # any module necessary for this one to work correctly
    'depends': ['point_of_sale','report_qweb_pdf_watermark'],

    # always loaded
    'data': [
        'reports/pos_print_config.xml',
        'reports/pos_print_report_background.xml',
    ], 
    'installable': True,
    'application': True,  
}