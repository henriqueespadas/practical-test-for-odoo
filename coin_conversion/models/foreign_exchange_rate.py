from odoo import models, fields

class AccountForeignExchangeRate(models.Model):
    _name = 'account.foreign.exchange.rate'

    date = fields.Date(string='Data')
    currency_from_id = fields.Many2one('res.currency', string='Moeda de Origem')
    currency_to_id = fields.Many2one('res.currency', string='Moeda de Destino')
    exchange_rate = fields.Float(string='Taxa de Câmbio')
