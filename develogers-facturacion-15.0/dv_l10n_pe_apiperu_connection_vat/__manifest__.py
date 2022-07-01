{
    'name': """
        Consulta RUC y DNI con Integración a ApiPeru Perú
    """,

    'summary': """
        Permite obtener datos del contacto registrando el DNI o RUC mediante una integración con ApiPeru.
    """,

    'description': """
        Adds withholding tax move in invoices and creates the account seat. |
        Agrega impuesto de retención en facturas y crea la cuenta de retención.
    """,

	'author': 'Develogers',
    'website': 'https://develogers.com',
    'support': 'especialistas@develogers.com',
    'live_test_url': 'https://demo.develogers.com',
    'license': 'LGPL-3',

    'category': 'Accounting',
    'version': '14.0',

    'price': 99.99,
    'currency': 'EUR',

    'depends': [
        'base',
        'l10n_pe',
    ],

    'data': [
		'security/ir.model.access.csv',
		'data/res_city_data.xml',
		'wizard/busqueda_view.xml',
		'views/company_view.xml',
		'views/res_partner_view.xml',
	],

    'images': ['static/description/banner.gif'],

    'application': True,
    'installable': True,
    'auto_install': False,
}