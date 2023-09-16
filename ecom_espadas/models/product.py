from odoo import models, fields


class Product(models.Model):
    _name = "ecom_espadas.product"

    name = fields.Char(required=True)
    price = fields.Float(required=True)
    stock_quantity = fields.Integer(required=True)
