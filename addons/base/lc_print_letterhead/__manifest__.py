# -*- coding: utf-8 -*-
{
    'name': "Add print Letterhead pos, sale, T_Expres",

    'summary': """
        Add print Letterhead pos, sale, T_Expres""",

    'description': """
        Add print Letterhead pos, sale, T_Expres.
    """,

    'author': "Labcit Inc.",
    'website': "http://www.labcit.com",
    
    'category': 'Manufacturing',
    'version': '14.0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale'],

    # always loaded
    'data': [        
        # 'security/groups.xml', 
        'reports/lc_print_letterhead.xml',        
        'reports/print_letterhead_sale_report_template.xml',        
    ], 
    'installable': True,
    'application': True,  
}