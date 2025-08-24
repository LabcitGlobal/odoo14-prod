# Part of Softhealer Technologies.

{
    "name": "POS Product Enlarge Image",
    "author": "Softhealer Technologies",
    "website": "https://www.softhealer.com",
    "support": "support@softhealer.com",
    "version": "14.0.2",
    "license": "OPL-1",
    "category": "Point Of Sale",
    "summary": "POS Product Enlarge Image, Point Of Sale Zoom Photo, POS Large Image Module, Make POS Picture Big App, POS Product Large Image, pos zoom photo, pos big image Odoo ",
    "description": """This module allows you to see a large product image from the POS interface. On clicking the enlarge image icon popup comes with a large product image with a description in point of sale.
 Point Of Sale Product Enlarge Image Odoo
 POS Product Enlarge Image Module, Point Of Sale Zoom Product Photo, POS Large Image, Make POS Picture Big, POS Product Large Image Odoo 
 POS Product Enlarge Image, Point Of Sale Zoom Photo, POS Large Image Module, Make POS Picture Big App, POS Product Large Image Odoo""",
    "depends": ["point_of_sale"],
    'data': [
        'views/assets.xml',
        'views/enlarge_image_view.xml',
    ],
    'qweb': ['static/src/xml/*.xml'],
    'images': ['static/description/background.png', ],
    "live_test_url": "https://youtu.be/R9x7mK26CQw",
    'auto_install': False,
    'installable': True,
    'application': True,
    "price": 10,
    "currency": "EUR"
}
