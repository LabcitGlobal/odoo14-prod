# -*- coding: utf-8 -*-
{
    'name': "Report Employee Attendance",

    'summary': """
        PDF report of an employee's attendance.""",

    'description': """
        It generates a PDF report of an employee's attendance, hours worked, delays, absences.
            Configure before using this module:
                1. Stable "Working Hours"
                2. Register and enable contracts
                3. Config postgresql.conf in /etc/postgresql/main/**/ timezone="America/La_Paz"
        
    """,

    'author': "Labcit Inc.",
    'website': "http://www.labcit.com",
    
    'category': 'Human Resources',
    'version': '14.0.1',

    # any module necessary for this one to work correctly
    'depends': ['hr','hr_attendance','hr_contract','lc_attendance_comment'],

    # always loaded
    'data': [
    #    'security/user_groups.xml',        
        'security/ir.model.access.csv',                   
        'views/views.xml',        
        'reports/lc_employee_report.xml',
        'reports/print_lc_employee_report_template.xml',        
    ], 
    'installable': True,
    'application': True,  
}