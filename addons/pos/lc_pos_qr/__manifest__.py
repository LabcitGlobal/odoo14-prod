# -*- coding: utf-8 -*-
{
    'name': "Payment in POS by QR",

    'summary': """
        Registration of qr image to print on the sales note, the qr of payment of the order at the point of sale.""",

    'description': """
        Registration of qr image to print on the sales note, the qr of payment of the order at the point of sale.
    """,

    'author': "Labcit Inc",
    'website': "http://www.labcit.com",
    'category': 'Point Of Sale',    
    'version': '14.0.1',
    'depends': ['point_of_sale'],    
    'data': [        
        'security/ir.model.access.csv',
        'views/view_pos_qr.xml',
        'reports/pos_qr_print.xml',
        'reports/pos_qr_print_report_template.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}