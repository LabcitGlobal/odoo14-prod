# -*- coding: utf-8 -*-
{
    'name': "lc_pos_margin_label",

    'summary': """
        Superponer una propiedad a la imagen en el POS""",

    'description': """
        Superponer una propiedad a la imagen en el POS
    """,

    'author': "Labcit Inc",
    'website': "http://www.labcit.com",
    'category': 'Point Of Sale',    
    'version': '14.0.1',
    'depends': ['point_of_sale'],    
    'data': [        
        'views/lc_pos_image_label.xml',            
        'views/lc_pos_template_view.xml',
        'views/lc_product_variant_label.xml',
    ],
    'qweb': ['static/src/xml/pos_view.xml'],
    
    'installable': True,
    'application': True,
    'auto_install': False,
}