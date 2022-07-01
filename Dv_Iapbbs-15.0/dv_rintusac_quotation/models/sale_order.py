from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    atention = fields.Many2one('res.partner', string="Atención")
    requirement = fields.Char(string="Requerimiento")

    mrp_production_available_ids = fields.Many2many('mrp.production', 'sale_mrp_available_rel', 'sale_id', 'mrp_prod_id',
                                                    compute="_compute_mrp_production_available_ids", store=True)
    sucursal = fields.Char(string="Sucursal")
    @api.depends('partner_id')
    def _compute_mrp_production_available_ids(self):
        for record in self:
            record.mrp_production_available_ids = self.env['mrp.production'].search([
                ('partner_id', '=', record.partner_id.id)
            ]).ids

    mrp_production_ids = fields.Many2many(
        'mrp.production', 'sale_order_mrp_production_rel', 'sale_order_id', 'mrp_production_id', string="RM")
    
    mrp_production_name = fields.Char(string="RM", compute="_compute_mrp_production_name", store=True)
    @api.depends('mrp_production_ids')
    def _compute_mrp_production_name(self):
        for record in self:
            record.mrp_production_name = '-'.join(record.mrp_production_ids.mapped('name'))
    
    partner_guide_available_ids = fields.Many2many('partner.guide', 'sale_partner_guide_available_rel', 'sale_id', 'partner_guide_id',
                                                    compute="_compute_partner_guide_available_ids", store=True)
    @api.depends('partner_id')
    def _compute_partner_guide_available_ids(self):
        for record in self:
            record.partner_guide_available_ids = self.env['partner.guide'].search([
                ('partner_id', '=', record.partner_id.id)
            ]).ids
    partner_guide_id = fields.Many2one('partner.guide', string="G/R")