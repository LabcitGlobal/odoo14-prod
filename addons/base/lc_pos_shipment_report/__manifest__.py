# -*- coding: utf-8 -*-
{
    'name': "POS Shipment Printing Report",

    'summary': """
        Generate POS Shipment Printing Report""",

    'description': """
        Generate POS Shipment Printing Report
    """,

    'author': "Labcit Inc",
    'website': "http://www.labcit.com",
    'category': 'Point of Sale',    
    'version': '14.0.0',
    'depends': ['point_of_sale'],    
    'data': [
        'security/ir.model.access.csv',
        'wizards/pos_shipment_view.xml',        
        'reports/lc_pos_shipment_report.xml',
        'reports/print_lc_pos_shipment_report_template.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}