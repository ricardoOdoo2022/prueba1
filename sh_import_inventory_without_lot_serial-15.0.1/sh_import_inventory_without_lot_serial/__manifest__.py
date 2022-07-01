# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.
{
    "name": "Import Inventory Without Lot-Serial From CSV-Excel File | Import Inventory Without Lot From CSV | Import Inventory Without Lot From Excel | Import Inventory Without Serial Number From CSV | Import Inventory Without Serial Number From Excel",
    "author": "Softhealer Technologies",
    "website": "https://www.softhealer.com",
    "support": "support@softhealer.com",
    "version": "15.0.1",
    "category": "Warehouse",
    "summary": "Import Stock From CSV Import Stock From Excel Import Inventory From CSV import Inventory From Excel Import Stock Without Lot Stock Without Serial Import Multiple Inventory Import Inventory From XLS Inventory Without Lot Inventory Without Serial Odoo",
    "description": """This module is useful to import inventory(stock) without lot/serial number from CSV/Excel file. """,
    "depends": [
        'stock',
        'sh_message',
    ],
    "data": [
        'security/import_inventory_without_lot_serial_security.xml',
        'security/ir.model.access.csv',
        'wizard/import_inventory_without_lot_serial_wizard.xml',
        'views/stock_view.xml',
    ],
    "images": ["static/description/background.png", ],
    "license": "OPL-1",
    "installable": True,
    "auto_install": False,
    "application": True,
    "price": "15",
    "currency": "EUR"
}
