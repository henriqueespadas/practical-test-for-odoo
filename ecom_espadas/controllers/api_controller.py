from odoo import http


class EcommerceAPI(http.Controller):
    @http.route(["/api/product"], type="json", auth="public", website=True)
    def list_products(self):
        products_list = http.request.env["ecom_espadas.product"]
        products = products_list.search([])
        return {"products": [(p.id, p.name) for p in products]}

    @http.route("/api/cart/add", type="json", auth="public", website=True)
    def add_to_cart(self):
        json_data = http.request.jsonrequest
        product_id = json_data.get("product_id")
        quantity = json_data.get("quantity")

        if product_id is None or quantity is None:
            return {"status": "failure", "message": "Invalid parameters"}

        instance_cart = http.request.env["ecom_espadas.cart"]
        cart = instance_cart.get_or_create_cart()
        cart.add_product(product_id, quantity)
        return {"status": "success"}
