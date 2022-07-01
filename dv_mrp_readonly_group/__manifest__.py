{
    'name': """
        MRP Production Read Only User |
    """,

    'summary': """
        SUMMARY. |
    """,

    'description': """
        DESCRIPTION. |
    """,

    'author': 'Develogers',
    'website': 'https://develogers.com',
    'support': 'especialistas@develogers.com',
    'live_test_url': 'https://demo.develogers.com',
    'license': 'LGPL-3',

    'category': 'Invoice',
    'version': '14.0',

    'depends': [
        'base',
        'mrp',
    ],

    'data': [
        'security/res_groups_data.xml',
        'security/ir.model.access.csv',
        'views/menuitem_views.xml',
        'views/mrp_production_views.xml',
    ],
    
    "assets": {
    },

    'images': ['static/description/banner.gif'],
    
    'application': True,
    'installable': True,
    'auto_install': False,
}
