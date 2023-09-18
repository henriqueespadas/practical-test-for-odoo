from odoo import models, fields, api

class InvoiceAPIConfig(models.TransientModel):
    _name = 'invoice.api.config'
    _description = 'Invoice API Configuration'

    api_endpoint = fields.Char(string='API Endpoint URL')

    @api.model
    def get_default_values(self, fields):
        api_endpoint = self.env['ir.config_parameter'].sudo().get_param('api_endpoint')
        return {'api_endpoint': api_endpoint}

    def set_values(self):
        self.env['ir.config_parameter'].sudo().set_param('api_endpoint', self.api_endpoint)
