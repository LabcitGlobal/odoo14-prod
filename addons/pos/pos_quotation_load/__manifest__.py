# Part of Softhealer Technologies.
{
    "name": "POS Quotation Load",
    "author": "Softhealer Technologies",
    "website": "https://www.softhealer.com",
    "support": "support@softhealer.com",
    "category": "Point of Sale",
    "summary": "POS Quotation Load Odoo, POS Order So Load Odoo, Point Of Sale Quotation Load,POS Sales Order Load,POS quotation Analysis Module, Point Of Sale SO Load App, POS Load Sale Order Odoo",
    "description": """Do you want to load a quotation to POS? Do you do that manually? so it's quite a time-consuming task, here we build a module to easily load a quotation in POS. Easy to sync quotation with the POS system. You will also easily search quotations in pos. We have also given a field in quotation to identify quotation sync with pos. You can also get a pos order reference number in the quotation. the quotation will be canceled automatically after the POS order is done.                            
POS Quotation Load Odoo, POS Order So Load Odoo.
Quotation Load  In Point Of Sale, Sales Order Load In POS Detail Report Odoo, Feature Of Load SO In POS Odoo.
POS quotation Analysis Module, Point Of Sale SO Load App, POS Load Sale Order Odoo.""",
    "version": "14.0.1",
    "license": "OPL-1",
    "depends": ["sale_management", "point_of_sale"],
    "application": True,
    "data": [
        'views/pos_custom_view.xml',
        'views/pos_order_custom_view.xml',
        'views/sale_order_custom.xml',
    ],
    "qweb": [
        "static/src/xml/*.xml",
    ],
    "images": ["static/description/background.jpg", ],
    "live_test_url": "https://youtu.be/P1ubbq5db50",
    "auto_install": False,
    "installable": True,
    "price": 25,
    "currency": "EUR"
}
