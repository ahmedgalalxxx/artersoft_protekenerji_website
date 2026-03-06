# -*- coding: utf-8 -*-
# Part of Protek Enerji. See LICENSE file for full copyright and licensing details.
{
    'name': 'Protek Enerji E-Commerce Portal',
    'version': '18.0.1.0.0',
    'category': 'Website/Website',
    'summary': 'Restricted E-Commerce Portal for Protek Enerji Customers',
    'description': """
Protek Enerji E-Commerce Portal
===============================
A custom e-commerce portal for Protek Enerji customers with restricted access.
    """,
    'author': 'Protek Enerji',
    'website': 'http://www.protekenerji.com/',
    'license': 'LGPL-3',
    'depends': [
        'website_sale',
        'website_sale_stock',
        'portal',
        'auth_signup',
        'payment',
    ],
    'data': [
        'security/ir.model.access.csv',
        'security/protekenerji_security.xml',
        'data/website_data.xml',
        'data/website_menu_data.xml',
        'views/templates/layout_templates.xml',
        'views/templates/home_templates.xml',
        'views/templates/shop_templates.xml',
        'views/templates/cart_templates.xml',
        'views/templates/checkout_templates.xml',
        'views/templates/orders_templates.xml',
        'views/templates/gdpr_templates.xml',
        'views/templates/login_templates.xml',
        'views/assets.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'protekenerji/static/src/scss/protekenerji.scss',
            'protekenerji/static/src/js/protekenerji.js',
        ],
    },
    'images': ['static/description/icon.svg'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
