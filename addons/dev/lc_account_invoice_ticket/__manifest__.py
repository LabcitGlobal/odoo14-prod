# -*- coding: utf-8 -*-
{
    'name': "Change Print Invoice to Ticket",

    'summary': """
        Change Print Invoice to Ticket""",

    'description': """
        Change Print Invoice to Ticket.
    """,

    'author': "Labcit Inc.",
    'website': "http://www.labcit.com",
    
    'category': 'Human Resources',
    'version': '14.0.1',

    # any module necessary for this one to work correctly
    'depends': ['account_accountant'],

    # always loaded
    'data': [
        'views/invoice_views.xml',        
    ], 
    'installable': True,
    'application': True,  
}