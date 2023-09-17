from odoo import api, fields, models


class AccountMove(models.Model):
    _inherit = 'account.move'

    currency_id = fields.Many2one('res.currency', string='Currency')

    @api.model
    def create(self, vals):
        record = super(AccountMove, self).create(vals)

        if record.currency_id and record.currency_id != record.company_id.currency_id:
            exchange_rate = self.env['account.foreign.exchange.rate'].search([
                ('currency_from_id', '=', record.currency_id.id),
                ('currency_to_id', '=', record.company_id.currency_id.id),
            ], limit=1, order='date desc')

            if exchange_rate:
                for line in record.line_ids:
                    original_amount = line.amount_currency
                    converted_amount = original_amount * exchange_rate.exchange_rate
                    line.write({'amount_currency': converted_amount})

        return record
