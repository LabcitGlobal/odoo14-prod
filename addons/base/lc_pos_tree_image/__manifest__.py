# -*- coding: utf-8 -*-
{
    'name': "Imprimir Boletas con imagenes en POS",

    'summary': """
        Modulo para reimprimir ordenes creadas en el POS con Imagen""",

    'description': """
        Modulo para reimprimir ordenes creadas en el POS con Imagen
    """,

    'author': "Labcit Inc",
    'website': "http://www.labcit.com",
    'category': 'Point Of Sale',    
    'version': '14.0.0.1',
    'depends': ['base','point_of_sale','hr'],    
    'data': [
        "reports/lc_pos_tree_print.xml",        
        "reports/pos_print_image_template.xml",        
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}