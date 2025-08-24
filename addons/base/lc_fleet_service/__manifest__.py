# -*- coding: utf-8 -*-
{
    'name': "Fleet Services Admin",

    'summary': """
        Module for fleet services admin""",

    'description': """
        Module for fleet services admin.
    """,

    'author': "Labcit Inc.",
    'website': "http://www.labcit.com",
    
    'category': 'Services',
    'version': '14.0.1',

    # any module necessary for this one to work correctly
    'depends': ['contacts','fleet','sequence_reset_period'],

    # always loaded
    'data': [
        'data/lc_file_category.xml',
        'data/lc_fleet_category_expenses.xml',
        'data/lc_fleet_remission_document_type.xml',        
        'data/lc_vehicle_parts_list.xml',        
        # 'security/user_groups.xml', 
        'security/ir.model.access.csv',        
        'views/fleet_service.xml',
        'views/fleet_remission.xml',
        'views/fleet_driver_expenses.xml',
        'views/fleet_tracking.xml',
        'views/fleet_bank_account.xml',
        'views/fleet_service_code.xml',
        'views/container_control.xml',
        'views/container_file.xml',
        'views/vehicle_parts_inventory.xml',
        'reports/menu_config_report.xml',
        'reports/fleet_service_report.xml',        
        'reports/fleet_service_quotation_report.xml',        
        'reports/fleet_remission_report.xml',        
        'reports/container_control_report.xml',        
        'reports/vehicle_parts_inventory_report.xml',        
    ], 
    'installable': True,
    'application': True,  
}