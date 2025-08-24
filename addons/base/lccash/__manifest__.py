# -*- coding: utf-8 -*-
{
    'name': "Gestion de Cajas",

    'summary': """
        Modulo para gestionar las transacciones de Caja""",

    'description': """
        Modulo para gestionar las transacciones de Caja, Cobros, Adelantos, Cambios, Reportes.
    """,

    'author': "Labcit Inc.",
    'website': "http://www.labcit.com",
    
    'category': 'Manufacturing',
    'version': '14.0.2',

    # any module necessary for this one to work correctly
    'depends': ['hr','point_of_sale','sale','purchase'],

    # always loaded
    'data': [
        'security/user_groups.xml',        
        'security/ir.model.access.csv',
        'data/lccash_money.xml',               
        'views/lccash_change_views.xml',
        'views/lccash_payment_views.xml',
        'views/lccash_withdraw_views.xml',
        'reports/lccash_report.xml',
        'reports/lccash_detail_reports.xml',
        'reports/lccash_day_reports.xml',         
    ], 
    'installable': True,
    'application': True,  
}