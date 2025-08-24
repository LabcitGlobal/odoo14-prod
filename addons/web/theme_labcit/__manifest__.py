# -*- coding: utf-8 -*-
{
    'name': "Theme Labcit",

    'summary': """
        Labcit corporate website frontend template """,

    'description': """
        Labcit corporate website frontend template
    """,

    'author': "Labcit",
    'website': "https://www.labcit.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Theme/Services',
    'version': '14.0.1',

    # any module necessary for this one to work correctly
    'depends': ['website'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/assets.xml',
        'views/header.xml',
        'views/footer.xml',
        'views/layouts.xml',
        'views/snippets/slider.xml',
        'views/snippets/money.xml',
        'views/snippets/about.xml',
        'views/snippets/partner.xml',
        'views/landingpage.xml',
    ],
    'images': [
        'static/description/theme_screenshot.jpg',
    ],

    'installable': True,
    'application': False,
    'auto_install': False,
}
