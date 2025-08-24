# -*- coding: utf-8 -*-
{
    'name': "Add print pos, sale, T_Ex",

    'summary': """
        Add print pos, sale, T_Ex""",

    'description': """
        Add print pos, sale, T_Ex.
    """,

    'author': "Labcit Inc.",
    'website': "http://www.labcit.com",
    
    'category': 'Manufacturing',
    'version': '14.0.1',

    # any module necessary for this one to work correctly
    'depends': ['point_of_sale','sale'],

    # always loaded
    'data': [        
        'security/groups.xml', 
        'reports/lc_pos_reprint.xml',        
        'reports/pos_report_template_tex.xml',        
        'reports/sale_report_template_tex.xml',        
    ], 
    'installable': True,
    'application': True,  
}