# -*- coding: utf-8 -*-
{
    'name': "HR Attendance Comment",

    'summary': """
        Add field Comment in HR Attendance""",

    'description': """
        Add field Comment in HR Attendance.
    """,

    'author': "Labcit Inc.",
    'website': "http://www.labcit.com",
    
    'category': 'Human Resources',
    'version': '14.0.1',

    # any module necessary for this one to work correctly
    'depends': ['hr_attendance'],

    # always loaded
    'data': [                       
        'views/lc_attendace_comment.xml',                         
    ], 
    'installable': True,
    'application': True,  
}