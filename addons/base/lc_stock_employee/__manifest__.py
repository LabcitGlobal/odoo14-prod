# -*- coding: utf-8 -*-
{
    'name': "Stock Employee",

    'summary': """
        Add responsibility of the stock to the employee by category""",

    'description': """
        Add responsibility of the stock to the employee by category
    """,

    'author': "Labcit Inc",
    'website': "http://www.labcit.com",
    'category': 'Warehouse Management',    
    'version': '14.0.1',
    'depends': ['stock'],    
    'data': [
        'security/ir.model.access.csv',
        'views/lc_stock_employee.xml',
        'views/lc_stock_employee_report.xml',
        'reports/lc_stock_employee_report.xml',
        'reports/print_lc_stock_employee_report_template.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}