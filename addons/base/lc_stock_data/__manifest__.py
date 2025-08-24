# -*- coding: utf-8 -*-
{
    'name': "Stock Data",

    'summary': """
        List and print the inventory quantity on hand""",

    'description': """
        List and print the inventory quantity on hand
    """,

    'author': "Labcit Inc",
    'website': "http://www.labcit.com",
    'category': 'Inventory/Inventory',    
    'version': '14.0.1',
    'depends': ['stock'],    
    'data': [
        'security/ir.model.access.csv',
        'views/lc_view_stock_data.xml',
        'reports/lc_stock_data_report.xml',
        'reports/print_lc_stock_data_report_template.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}