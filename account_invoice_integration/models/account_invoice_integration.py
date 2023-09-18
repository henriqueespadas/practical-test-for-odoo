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
        print('Sending invoice to external system.')
        api_url = 'https://de798585-0b42-4765-b4f8-7f2c5230e8d9.mock.pstmn.io//api/invoices'

        payload = {
            'invoice_number': invoice.name,
            'amount': invoice.amount_total,
        }

        response = requests.post(api_url, json=payload)

        if response.status_code == 200:
            print("Successfully sent invoice to external system.")
        else:
            print("Failed to send invoice to external system.")

        vals = {
            'invoice_id': invoice.id,
            'status': 'success' if response.status_code == 200 else 'error',
            'response_message': response.text,
            'external_system_id': response.json().get('external_system_id') if response.status_code == 200 else '',
        }
        self.create(vals)
