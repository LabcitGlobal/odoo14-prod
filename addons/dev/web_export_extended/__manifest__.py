{
    'name': 'Web Export Password Protected',
    'category': 'Web',
    'summary': 'Display Export option the basis of Rights and Export is Password Protected.',
    'website': 'https://www.techultrasolutions.com',
    'version': '14.0.0.0',
    'description': """
Display Export option the basis of Rights and Export is Password Protected.
===================
        """,
    'author': 'TechUltra Solutions',
    'depends': ['web'],
    'installable': True,
    'data': [
        'security/web_export_security.xml',
        'views/web_export_templates.xml',
    ],
    'qweb': [
        'static/src/xml/*.xml',
    ],
    'application': False,
    'images': [
        'static/description/banner.jpg',
    ],
}
