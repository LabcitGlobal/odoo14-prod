# Copyright (C) Softhealer Technologies.
# Part of Softhealer Technologies.

{
    "name": "Point Of Sale Hide/Show Numpad",
    "author": "Softhealer Technologies",
    "license": "OPL-1",
    "website": "https://www.softhealer.com",
    "support": "support@softhealer.com",
    "category": "Point of Sale",
    "summary": "POS Hide Numpad, Point Of Sale Hide Numpad, Show/Hide POS Numpad, POS Hide Numpads, Disable POS Numpad, Remove Numpad, Point Of Sale Disable Numpad Odoo",
    "description": """Do you want to hide/show Numpad? Using this module, you can easily hide and show numpad in the POS. That's it. cheers!""",
    "version": "14.0.1",
    "depends": ["point_of_sale"],
    "application": True,
    "data": [
        'views/assets.xml',
        'views/pos_config.xml',
    ],
    "qweb": [
        'static/src/xml/*.xml',
    ],
    "images": ["static/description/background.png", ],
    "auto_install": False,
    "installable": True,
    "price": 15,
    "currency": "EUR"
}
