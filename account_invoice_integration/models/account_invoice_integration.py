from odoo import api, fields, models
import requests
import json


class AccountInvoiceIntegration(models.Model):
    _name = 'account.invoice.integration'
    _description = 'Invoice Integration'

    invoice_id = fields.Many2one('account.move', string='Invoice')
    external_system_id = fields.Char(string='External System ID')
    status = fields.Selection(
        [('pending', 'Pending'), ('success', 'Success'), ('error', 'Error')],
        string='Status'
    )
    response_message = fields.Text(string='Response Message')

    @api.model
    def _send_invoice_to_external_system(self, invoice):
        api_endpoint = self.env['ir.config_parameter'].sudo().get_param('api_endpoint')
        payload = {
            'invoice_number': invoice.name,
            'amount': invoice.amount_total,
        }

        response = requests.post(api_endpoint, json=payload)
        vals = {
            'invoice_id': invoice.id,
            'status': 'success' if response.status_code == 200 else 'error',
            'response_message': response.text,
            'external_system_id': response.json().get('external_system_id') if response.status_code == 200 else '',
        }
        self.create(vals)
