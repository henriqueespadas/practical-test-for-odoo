from odoo import models, fields, api


class OrderLine(models.Model):
    _name = "ecom_espadas.order_line"

    product_id = fields.Many2one("ecom_espadas.product")
    quantity = fields.Integer()
    order_id = fields.Many2one("ecom_espadas.order")
    subtotal = fields.Float(compute="_compute_subtotal")

    @api.depends("product_id", "quantity")
    def _compute_subtotal(self):
        for line in self:
            line.subtotal = line.product_id.price * line.quantity
