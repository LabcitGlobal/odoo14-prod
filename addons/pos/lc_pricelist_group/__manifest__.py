# -*- coding: utf-8 -*-
{
    'name': "Group Pricelist",

    'summary': """
        Update pricelist for Variant Group""",

    'description': """
        Update pricelist for Variant Group
    """,

    'author': "Labcit Inc.",
    'website': "http://www.labcit.com",
    'category': 'Point of Sale',
    'version': '1.0.1',

    'depends': ['point_of_sale'],

    'data': [
        'views/template_pricelist.xml',
        'views/views_pos_config.xml',
        'views/views_product_template.xml'
    ],
    'qweb': [
        'static/src/xml/pos_pricelist_group.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}