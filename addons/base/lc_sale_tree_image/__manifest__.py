# -*- coding: utf-8 -*-
{
    'name': "Imprimir Boletas con imagenes en Ventas",

    'summary': """
        Modulo para reimprimir ordenes creadas en el modulos Ventas con Imagen""",

    'description': """
        Modulo para reimprimir ordenes creadas en el modulo Ventas con Imagen
    """,

    'author': "Labcit Inc",
    'website': "http://www.labcit.com",
    'category': 'Point Of Sale',    
    'version': '14.0.0.1',
    'depends': ['base','sale','hr'],    
    'data': [
        "reports/lc_sale_tree_print.xml",        
        "reports/sale_print_image_template.xml",        
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}