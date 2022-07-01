from odoo import models, fields, api


class MrpProduction(models.Model):
    _inherit = 'mrp.production'
    partner_guide_available_ids = fields.Many2many('partner.guide',
                                                    compute="_compute_partner_guide_available_ids", store=True)
    @api.depends('partner_id')
    def _compute_partner_guide_available_ids(self):
        for record in self:
            record.partner_guide_available_ids = self.env['partner.guide'].search([
                ('partner_id', '=', record.partner_id.id)
            ]).ids
    partner_guide_id = fields.Many2one('partner.guide', string="G/R")
    product_type = fields.Selection([
        ('product', 'Product'),
        ('service', 'Service'),
        ('consu', 'Consumable')
    ], string='Tipo', default='product')
    product_available_ids = fields.Many2many('product.product',
                                             compute="_compute_product_available_ids", store=True)

    @api.depends('product_type')
    def _compute_product_available_ids(self):
        for record in self:
            record.product_available_ids = self.env['product.product'].search([
                ('type', '=', record.product_type),
                '|',
                ('company_id', '=', False),
                ('company_id', '=', self.env.company.id)
            ])

    product_id = fields.Many2one(
        'product.product', 'Product',
        domain="""[
            ('company_id', '=', False),
            ('company_id', '=', company_id)
        ]
        """,
        readonly=True, required=True, check_company=True,
        states={'draft': [('readonly', False)]})

    partner_id = fields.Many2one('res.partner', string="Cliente")
    commercial_user_id = fields.Many2one(
        'res.users', string="Asesor comercial")

    warranty_expiration_date = fields.Date(
        string="Fecha de vencimiento de garantía")
    warranty_state = fields.Selection([
        ('inactive', 'Inactivo'),
        ('active', 'Activo')
    ], string="Estado de garantía", compute='_compute_warranty_state', store=True)
    
    @api.depends('warranty_expiration_date')
    def _compute_warranty_state(self):
        for record in self:
            if record.warranty_expiration_date and record.warranty_expiration_date > fields.Date.today():
                warranty_state = 'active'
            else:
                warranty_state = 'inactive'
            record.warranty_state = warranty_state
                
