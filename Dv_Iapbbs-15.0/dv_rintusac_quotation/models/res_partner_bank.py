from odoo import models, fields, api, _


class ResPartnerBank(models.Model):
    _inherit = 'res.partner.bank'
    
    account_code = fields.Char(string="Codigo de Cuenta")
