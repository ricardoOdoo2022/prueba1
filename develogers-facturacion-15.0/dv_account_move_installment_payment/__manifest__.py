{
    'name': """
        Payment Installment Detail for Invoices |
        Detalle de Cuotas de pago para Facturas
    """,

    'summary': """
        Allows to see the payment installments of an invoice. |
        Permite visualisar las cuotas de pago de una factura. 
    """,

    'description': """
        Adds payment installments according to the terms of payment in customer invoices and supplier invoices. |
        Agrega cuotas de pago según los términos de pago en las facturas de clientes y proveedores.        
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
        'account',
    ],

    'data': [
        'views/account_move_views.xml',
        'security/ir.model.access.csv',
    ],
    
    'images': ['static/description/banner.gif'],
    
    'application': True,
    'installable': True,
    'auto_install': False,
}
