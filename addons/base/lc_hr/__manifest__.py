# -*- coding: utf-8 -*-
{
    'name': "Hr Contract and regulations",

    'summary': """
        Labor contract and internal regulations""",

    'description': """
        Labor contract and internal regulations.
    """,

    'author': "Labcit Inc.",
    'website': "http://www.labcit.com",
    
    'category': 'Human Resources',
    'version': '14.0.1',

    # any module necessary for this one to work correctly
    'depends': ['hr','hr_contract'],

    # always loaded
    'data': [
        'views/hr_contract_views.xml',
        'reports/menu_config_report.xml',
        'reports/hr_contract_report.xml',
        'reports/hr_regulation_report.xml',
    ], 
    'installable': True,
    'application': True,  
}