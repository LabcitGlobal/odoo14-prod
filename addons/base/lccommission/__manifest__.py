# -*- coding: utf-8 -*-
{
    'name': "Commission Agent",

    'summary': """
        Modulo para administrar Agentes de Venta y Entrega""",

    'description': """
        Modulo para administrar Agentes de Venta y Entrega.
    """,

    'author': "Labcit Inc.",
    'website': "http://www.labcit.com",
    
    'category': 'Manufacturing',
    'version': '14.0.1',

    # any module necessary for this one to work correctly
    'depends': ['point_of_sale'],

    # always loaded
    'data': [
        'security/groups.xml', 
        'security/ir.model.access.csv',
        'data/lccommission_type.xml',        
        'data/lccommission_type_agent.xml',        
        'views/lccommission_agent.xml',
        'views/lccommission_pos_agent.xml',
        'views/lccommission_pos_subagent.xml',
        'views/lccommission_pos_agent_view.xml',
        'views/lccommission_pos_subagent_view.xml',
        'views/lccommission_pos_file.xml',
        'views/lccommission_pos_file_view.xml',
        'wizard/posorder_agent_wizard.xml',
        'wizard/posorder_subagent_wizard.xml',
    ], 
    'installable': True,
    'application': True,  
}