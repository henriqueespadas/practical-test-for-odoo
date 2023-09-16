from odoo import models, fields, api


class Order(models.Model):
    _name = 'ecom_espadas.order'

    line_ids = fields.One2many('ecom_espadas.order_line', 'order_id')
    total_amount = fields.Float(compute='_compute_total_amount')

    @api.depends('line_ids')
    def _compute_total_amount(self):
        for order in self:
            order.total_amount = sum(line.subtotal for line in order.line_ids)
