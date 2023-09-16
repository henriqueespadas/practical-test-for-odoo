from odoo import models, fields, api


class Cart(models.Model):
    _name = "ecom_espadas.cart"

    line_ids = fields.One2many("ecom_espadas.cart_line", "cart_id")
    total_amount = fields.Float(compute="_compute_total_amount")

    @api.depends("line_ids")
    def _compute_total_amount(self):
        for cart in self:
            cart.total_amount = sum(line.subtotal for line in cart.line_ids)

    def checkout(self):
        order = self.env["ecom_espadas.order"].create(
            {
                "line_ids": [
                    (
                        0,
                        0,
                        {"product_id": line.product_id.id, "quantity": line.quantity},
                    )
                    for line in self.line_ids
                ]
            }
        )
        self.line_ids.unlink()
        return order.id

    def get_or_create_cart(self):
        user_id = self.env.uid
        cart = self.search([("create_uid", "=", user_id)], limit=1)
        if cart:
            return cart
        else:
            return self.create({})

    def add_product(self, product_id, quantity):
        cart_line = self.env["ecom_espadas.cart_line"]
        existing_line = cart_line.search(
            [("product_id", "=", product_id), ("cart_id", "=", self.id)], limit=1
        )
        if existing_line:
            existing_line.quantity += quantity
        else:
            cart_line.create(
                {"product_id": product_id, "quantity": quantity, "cart_id": self.id}
            )
