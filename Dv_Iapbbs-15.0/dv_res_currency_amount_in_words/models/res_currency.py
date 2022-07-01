from odoo import fields, models, api, _
from num2words import num2words

class ResCurrency(models.Model):
    _inherit = 'res.currency'

    def convert_amount_to_words(self, amount):
        amount_base, amount = divmod(amount, 1)
        amount = round(amount, 2)
        amount = int(round(amount * 100, 2))

        lang_code = self.env.context.get('lang') or self.env.user.lang
        lang = self.env['res.lang'].search([('code', '=', lang_code)])
        words = num2words(amount_base, lang=lang.iso_code)
        result = _('%(words)s CON %(amount)02d/100 %(currency_label)s') % {
            'words': words,
            'amount': amount,
            'currency_label': self.name == 'PEN' and 'SOLES' or self.currency_unit_label,
        }
        amount_in_words = result.upper()
        return amount_in_words
    
