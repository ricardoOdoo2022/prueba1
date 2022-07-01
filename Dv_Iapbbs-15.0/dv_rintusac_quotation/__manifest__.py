{
    'name': """
        Rintusac App |
    """,

    'summary': """

    """,

    'description': """

    """,

    'author': 'Develogers',
    'website': 'https://develogers.com',
    'support': 'especialistas@develogers.com',
    'live_test_url': 'https://demo.develogers.com',
    'license': 'LGPL-3',

    'category': 'Invoice',
    'version': '1.0',

    'price': 39.99,
    'currency': 'EUR',

    'depends': [
        'base',
        'mrp',
        'sale_management',
        'stock',
        'dv_sale_order_amount_total_in_words',
    ],

    'data': [
        'security/ir.model.access.csv',
        'views/mrp_production_views.xml',
        'views/res_partner_views.xml',
        'views/sale_order_views.xml',
        'views/stock_picking_views.xml',
        'templates/external_layout_standard.xml',
        'templates/report_saleorder_document.xml',
    ],
    
    'images': ['static/description/banner.gif'],
    
    'application': True,
    'installable': True,
    'auto_install': False,
}
