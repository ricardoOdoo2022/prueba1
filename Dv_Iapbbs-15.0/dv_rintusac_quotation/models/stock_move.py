from odoo import models, fields, api


class StockMove(models.Model):
    _inherit = 'stock.move'
    
    product_id = fields.Many2one(
        'product.product', 'Product',
        check_company=True,
        domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]", index=True, required=True,
        states={'done': [('readonly', True)]})