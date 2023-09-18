from odoo import api, fields, models

class AccountMove(models.Model):
    _inherit = 'account.move'

    @api.model_create_multi
    def create(self, vals_list):
        invoices = super(AccountMove, self).create(vals_list)
        for invoice in invoices:
            if invoice.state == 'posted':
                self.env['account.invoice.integration']._send_invoice_to_external_system(invoice)
        return invoices

    def write(self, vals):
        result = super(AccountMove, self).write(vals)
        for invoice in self:
            if invoice.state == 'posted':
                self.env['account.invoice.integration']._send_invoice_to_external_system(invoice)
        return result
