from xmlrpc.client import boolean
from odoo import models, fields, api, _
from odoo.exceptions import UserError

class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    _sql_constraints = [
        ('internal_code_uniq', 'UNIQUE (internal_code)', '¡No puedes tener dos Productos con el mismo Codigo Interno!')
    ]

    internal_code = fields.Char(string='Codigo Interno')
    part_number  = fields.Char(string='Numero de Parte')
    equivalent_code=fields.Char(string='Codigo Equivalente')
    ledger_account = fields.Many2one(string='Cuenta contable', comodel_name='account.account')
    isc = fields.Float(string='% ISC')
    item_type =fields.Selection(selection=[("nacional","Nacional"),("extrangero","Extrangero")],string="Tipo Articulo")
    model=fields.Char(string='Modelo')
    wide = fields.Float(string='Ancho')
    long_id = fields.Float(string='Largo')
    state = fields.Boolean(string='Estado')
   


    
   

    
    