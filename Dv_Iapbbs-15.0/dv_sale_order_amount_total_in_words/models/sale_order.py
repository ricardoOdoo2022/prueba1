from odoo import models, fields, api, _


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    amount_total_in_words = fields.Char(
        string='Amount Total in Words', compute='_compute_amount_total_in_words', store=True)

    @api.depends('amount_total', 'currency_id')
    def _compute_amount_total_in_words(self):
        for record in self:
            amount_total_in_words = record.currency_id.convert_amount_to_words(
                record.amount_total)
            record.amount_total_in_words = amount_total_in_words
