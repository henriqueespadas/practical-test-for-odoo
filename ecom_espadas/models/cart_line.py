from odoo import models, fields, api


class CartLine(models.Model):
    _name = 'ecom_espadas.cart_line'

    product_id = fields.Many2one('ecom_espadas.product')
    quantity = fields.Integer()
    cart_id = fields.Many2one('ecom_espadas.cart')
    subtotal = fields.Float(compute='_compute_subtotal')

    @api.depends('product_id', 'quantity')
    def _compute_subtotal(self):
        for line in self:
            line.subtotal = line.product_id.price * line.quantity


