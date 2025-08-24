# -*- coding: utf-8 -*-
{
    'name': "Imprimir Catalogo",

    'summary': """
        Imprimir Catalogo""",

    'description': """
        Imprimir Catalogo
    """,

    'author': "Labcit Inc",
    'website': "http://www.labcit.com",
    'category': 'Point Of Sale',    
    'version': '14.0.0.1',
    'depends': ['stock'],    
    'data': [
        "reports/pricelist_report.xml",        
        "reports/pricelist_report_template.xml",        
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}