from odoo import http


class EcommerceAPI(http.Controller):

    @http.route('/api/product', type='json', auth='public')
    def list_products(self):
        Product = http.request.env['ecom_espadas.produto']
        products = Product.search([])
        return {
            'products': [(p.id, p.nome) for p in products]
        }

    @http.route('/api/cart/add', type='json', auth='user')
    def add_to_cart(self, product_id, quantity):
        Cart = http.request.env['ecom_espadas.carrinho']
        cart = Cart._your_method_to_get_or_create_cart()
        cart.add_product(product_id, quantity)
        return {'status': 'success'}


