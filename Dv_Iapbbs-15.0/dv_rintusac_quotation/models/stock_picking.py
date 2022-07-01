from odoo import models, fields, api


class PartnerGuide(models.Model):
    _name = 'partner.guide'
    _description = 'Guía de Remisión'

    name = fields.Char(string="G/R", required=True)
    
    stock_picking_id = fields.Many2one('stock.picking', string="Albarán", compute="_compute_stock_picking_id")
    def _compute_stock_picking_id(self):
        for record in self:
            stock_picking_id = self.env['stock.picking'].search([
                ('partner_guide_id', '=', record.id)
            ], limit=1)
            record.stock_picking_id = stock_picking_id.id
    
    partner_id = fields.Many2one('res.partner', string="Cliente", compute="_compute_partner_id")
    def _compute_partner_id(self):
        for record in self:
            partner_id = record.stock_picking_id.partner_id
            record.partner_id = partner_id

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    partner_guide_id = fields.Many2one('partner.guide', string="G/R")
