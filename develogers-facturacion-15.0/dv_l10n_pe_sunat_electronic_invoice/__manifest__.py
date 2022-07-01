{
    'name': """
		Emisión de Facturas Electrónicas Sunat mediante Certificado Digital Perú
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

    'price': 499.99,
    'currency': 'EUR',

    'depends': [
                'dv_l10n_pe_sunat_catalog',
                'dv_l10n_pe_account_base',
                'account_debit_note',
    ],

    'data': [
        'security/solse_pe_cpe_security.xml',
        'security/ir.model.access.csv',
        'data/cpe_data.xml',
        'data/tareas_programadas.xml',
        'data/template_email_cpe.xml',
        'views/account_move_view.xml',
        'views/cpe_certificate_view.xml',
        'views/cpe_server_view.xml',
        'views/company_view.xml',
        'views/cpe_view.xml',
        'views/account_payment_term_view.xml',
        'report/report_invoice.xml',
        'report/report_invoice_ticket.xml',
        'wizard/account_invoice_debit_view.xml',
    ],

    'assets': {
        'web.report_assets_common': [
            'dv_l10n_pe_sunat_electronic_invoice/static/src/css/reportes.css',
        ]
    },

    'images': ['static/description/banner.gif'],

    'application': True,
    'installable': True,
    'auto_install': False,
}
