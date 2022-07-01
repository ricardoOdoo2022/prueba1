{
	'name': """
		Emisión de Guías Electrónicas Sunat mediante Certificado Digital Perú
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

    'price': 199.99,
    'currency': 'EUR',

	'depends': [
		'stock',
		'fleet',
		'account',
		'account_fleet',
		'product_expiry',
		'dv_l10n_pe_sunat_electronic_invoice',
	],
	'data': [
		'security/ir.model.access.csv',
		
		'views/company_view.xml',
  		'views/pe_sunat_eguide_view.xml',
    	'views/report_invoice.xml',
     	'views/res_partner.xml',
		'views/stock_view.xml',
		'data/sunat_eguide_data.xml',
		#'report/report_picking.xml',
		'report/report_guia.xml',
		
	],

	'images': ['static/description/banner.gif'],

    'application': True,
    'installable': True,
    'auto_install': False,
}