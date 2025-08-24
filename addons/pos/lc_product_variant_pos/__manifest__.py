# -*- coding: utf-8 -*-
{
    'name': "Enable product variants in pos",

    'summary': """
        Enable product variants in pos""",

    'description': """
        Enable product variants in pos
    """,

    'author': "Labcit Inc.",
    'website': "http://www.labcit.com",
    'category': 'Point of Sale',
    'version': '1.0.1',

    'depends': ['point_of_sale'],

    'data': [
        'views/assets.xml',
        'views/views_product_product.xml'
    ],
    'qweb': [
        'static/src/xml/pos_view.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}