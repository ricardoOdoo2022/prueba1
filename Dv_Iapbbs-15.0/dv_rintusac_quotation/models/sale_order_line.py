from odoo import models, fields, api, _


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    product_notes = fields.Text(string="Nota")


from odoo import fields, models, api
import odoo.addons.decimal_precision as dp


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def _total_discount(self):
        for rec in self:
            discount_amount = 0
            for line in rec.order_line:
                discount_amount += line.discount_amount
            rec.discount_amount = discount_amount
            rec.avg_discount = (discount_amount*100)/rec.amount_untaxed if rec.amount_untaxed else 0

    discount_amount = fields.Float('Total Disocunt', compute="_total_discount", digits=dp.get_precision('Discount'))
    avg_discount = fields.Float('Avg Disocunt', compute="_total_discount", digits=dp.get_precision('Discount'))
    print_discount = fields.Boolean('Print Discount')
    print_discount_amount = fields.Boolean('Print Discount Amount')

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    def _total_discount(self):
        for rec in self:
            discount = ((rec.discount*rec.price_unit)/100)
            rec.discount_per_unit = discount
            rec.discount_amount = discount*rec.product_uom_qty
            rec.discounted_unit_price = rec.price_unit - discount

    discount_amount = fields.Float('Disocunt Amount', compute="_total_discount", digits=dp.get_precision('Discount'))
    discount_per_unit = fields.Float('Discount Per Unit', compute="_total_discount", digits=dp.get_precision('Discount'))
    discounted_unit_price = fields.Float('Discounted Unit Price', compute="_total_discount", digits=dp.get_precision('Discount'))
    multi_discount = fields.Char('Discounts')
    
    aditional_discount_1 = fields.Float('Discount', digits=dp.get_precision('Discount'))
    aditional_discount_2 = fields.Float('Extra Discount', digits=dp.get_precision('Discount'))
    
    @api.onchange('aditional_discount_1','aditional_discount_2')
    def _onchange_multi_discount(self):
        def get_disocunt(percentage,amount):
            new_amount = (percentage * amount)/100
            return (amount - new_amount)
        if not self.aditional_discount_1 and not self.aditional_discount_2:
            self.discount = 0
        else:
            amount = 100
            if self.aditional_discount_1 and not self.aditional_discount_2:
                amount = get_disocunt(float(self.aditional_discount_1),amount)
                self.discount = 100 - amount
            elif self.aditional_discount_2 and not self.aditional_discount_1:
                amount = get_disocunt(float(self.aditional_discount_2),amount)
                self.discount = 100 - amount
            elif self.aditional_discount_1 and self.aditional_discount_2:
                amount = get_disocunt(float(self.aditional_discount_1),amount)
                amount = get_disocunt(float(self.aditional_discount_2),amount)
                self.discount = 100 - amount
            
            