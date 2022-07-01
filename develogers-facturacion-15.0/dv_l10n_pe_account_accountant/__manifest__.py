{
	'name': """
		Contabilidad para Localizacion Peruana
    """,

    'summary': """
        
    """,

    'description': """
        
    """,

	'author': 'Develogers',
    'website': 'https://develogers.com',
    'support': 'especialistas@develogers.com',
    'live_test_url': 'https://demoperu.develogers.com',
    'license': 'LGPL-3',

    'price': 99.99,
    'currency': 'EUR',

	'depends': [
		'account',
        'l10n_latam_invoice_document',
		'dv_l10n_pe_account_base',
	],
	'data': [
		'views/res_config_settings_view.xml',
		'views/account_move_view.xml',
		'views/res_partner_view.xml',
		'wizard/account_payment_register_views.xml',
	],
	
 	'images': ['static/description/banner.gif'],

    'application': True,
    'installable': True,
    'auto_install': False,
}