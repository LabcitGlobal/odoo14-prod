# -*- coding: utf-8 -*-
{
    'name': "Labcit Servicio Tecnico",

    'summary': """
        Modulo para administrar el departamento de Servicio Tecnico""",

    'description': """
        Modulo para administrar el departamento de Servicio Tecnico, Equipo,
        Diagnostico, Seguimiento.
    """,

    'author': "Labcit Inc.",
    'website': "http://www.labcit.com",
    
    'category': 'Manufacturing',
    'version': '14.0.1',

    # any module necessary for this one to work correctly
    'depends': ['hr'],

    # always loaded
    'data': [
        'security/user_groups.xml', 
        'security/ir.model.access.csv',
        'report/service_order_templates.xml',
        'report/service_order_views.xml',
        'views/lcsupport_machine_views.xml',
        'views/lcsupport_service_views.xml',        
    ], 
    'installable': True,
    'application': True,  
}