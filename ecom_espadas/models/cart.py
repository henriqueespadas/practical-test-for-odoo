from odoo import models, fields, api


class Cart(models.Model):
    _name = 'ecom_espadas.cart'

    line_ids = fields.One2many('ecom_espadas.cart_line', 'cart_id')
    total_amount = fields.Float(compute='_compute_total_amount')

    @api.depends('line_ids')
    def _compute_total_amount(self):
        for cart in self:
            cart.total_amount = sum(line.subtotal for line in cart.line_ids)

    def checkout(self):
        order = self.env['ecom_espadas.order'].create({
            'line_ids': [(0, 0, {'product_id': line.product_id.id, 'quantity': line.quantity}) for line in self.line_ids]
        })
        self.line_ids.unlink()
        return order.id
