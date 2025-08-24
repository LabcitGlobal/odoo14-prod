# -*- coding: utf-8 -*-
{
    'name': "Export Product All Images",

    'summary': """
        Export Product All Images""",

    'description': """
        Export Product All Images
    """,

    'author': "Labcit Inc",
    'website': "http://www.labcit.com",
    'category': 'Inventory',    
    'version': '14.0.0.1',
    "depends": ["stock", "web", "website_sale"],
    "data": [
        "security/product_export_images_groups.xml",
        "security/ir.model.access.csv",
        "data/product_export_images.xml",
    ],    
    "installable": True,
    "auto_install": False,
    "application": False,

}