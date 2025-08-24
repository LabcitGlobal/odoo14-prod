# -*- coding: utf-8 -*-
{
    'name': "Control de Nit,Dosificacion,Talonarios y facturas",

    'summary': """
        Modulo para llevar el control de Nit,Dosificacion,Talonarios y facturas""",

    'description': """
        Modulo para llevar el control de Nit,Dosificacion,Talonarios y facturas
    """,

    'author': "Labcit Inc.",
    'website': "http://www.labcit.com",        
    'category': 'Account',
    'version': '14.0.1',

    'depends': ['account'],
    
    'data': [        
        'security/ir.model.access.csv',                
        'views/lc_impuesto_nit.xml',        
        'views/lc_impuesto_dosificacion.xml',        
        'views/lc_impuesto_talonario.xml',        
        'views/lc_impuesto_venta.xml',        
        'views/lc_impuesto_compra.xml',        
    ],     
    'installable': True,
    'application': True,
    'auto_install': False,
}