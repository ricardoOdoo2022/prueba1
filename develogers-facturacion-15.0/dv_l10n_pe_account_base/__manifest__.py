{
	'name': """
		Contabilidad Base para Localizacion Peruana
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
		'base',
		'account',
		'l10n_pe',
		'l10n_latam_invoice_document',
  		'dv_account_invoice_date_currency_rate',
		'dv_l10n_pe_sunat_catalog',
  		'dv_account_move_installment_payment',
	],
	'data': [
		'security/pe_datas_security.xml',
		'security/ir.model.access.csv',
		'data/account_tax_data.xml',
		'data/l10n_latam_document_type_data.xml',
		'data/res_currency_data.xml',
		'views/l10n_latam_document_type_view.xml',
		'views/company_view.xml',
		'views/accoun_move_view.xml',
		'views/product_view.xml',
	],

	'images': ['static/description/banner.gif'],

    'application': True,
    'installable': True,
    'auto_install': False,
}
