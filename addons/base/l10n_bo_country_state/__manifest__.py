# -*- coding: utf-8 -*-
{
    'name': "Bolivian Country State",

    'summary': """
        Departments, Provinces, Municipalities for Bolivian Country State""",

    'description': """
        Departments, Provinces, Municipalities for Bolivian Country State.
    """,

    'author': "Labcit Inc.",
    'website': "http://www.labcit.com",

    'category': 'Localization',
    'version': '14.0.0',

    # any module necessary for this one to work correctly
    'depends': ['contacts'],

    # always loaded
    'data': [
        'data/res_country_states.xml',
        'data/res_country_province.xml',
        'data/res_country_municipalities.xml',
        'data/res_country_districts.xml',
        'security/ir.model.access.csv',
        'views/views_res_country_province.xml',
        'views/views_res_country_municipalities.xml',
        'views/views_res_country_district.xml',
        'views/views_res_country_menu.xml',
    ],
    'installable': True,
    'application': True,
}