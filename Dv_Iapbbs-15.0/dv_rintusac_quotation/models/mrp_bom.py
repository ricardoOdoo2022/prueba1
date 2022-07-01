from odoo import models, fields, api


class MrpBom(models.Model):
    _inherit = 'mrp.bom'
    
    product_id = fields.Many2one(
        'product.product', 'Product Variant',
        check_company=True, index=True,
        domain="[('product_tmpl_id', '=', product_tmpl_id),  '|', ('company_id', '=', False), ('company_id', '=', company_id)]",
        help="If a product variant is defined the BOM is available only for this product.")
    
class MrpWorkorder(models.Model):
    _inherit = 'mrp.workorder'
    
    technician_id = fields.Many2one('res.partner', string="Técnico", domain=[
                                    ('is_technician', '=', True)])