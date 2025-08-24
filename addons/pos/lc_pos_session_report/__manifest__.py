# -*- coding: utf-8 -*-
{
    'name': "Pos Session Report",

    'summary': """
        Generate Pos Session Report""",

    'description': """
        Generate Pos Session Report
    """,

    'author': "Labcit Inc",
    'website': "http://www.labcit.com",
    'category': 'Point of Sale',    
    'version': '14.0.0',
    'depends': ['point_of_sale'],    
    'data': [
        'security/ir.model.access.csv',
        'wizards/pos_session_view.xml',        
        'reports/lc_pos_session_report.xml',
        'reports/print_lc_pos_session_report_template.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}