from odoo import api, fields, models

class AccountMove(models.Model):
    _inherit = 'account.move'

    @api.model_create_multi
    def create(self, vals_list):
        invoices = super(AccountMove, self).create(vals_list)
        print('Invoices created.')
        for invoice in invoices:
            print('dentro for')
            if invoice.state == 'posted':
                print('Invoice is posted during creation. Initiating integration.')
                self.env['account.invoice.integration']._send_invoice_to_external_system(invoice)
        return invoices

    def write(self, vals):
        result = super(AccountMove, self).write(vals)
        print('Invoices writed.')
        for invoice in self:
            print('dentro for 2')
            if invoice.state == 'posted':
                print('Invoice is posted during update. Initiating integration.')
                self.env['account.invoice.integration']._send_invoice_to_external_system(invoice)
        return result
