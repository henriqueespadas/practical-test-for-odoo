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

    @http.route("/api/cart/remove", type="json", auth="public", website=True)
    def remove_from_cart(self):
        json_data = http.request.jsonrequest
        product_id = json_data.get("product_id")

        if product_id is None:
            return {"status": "failure", "message": "Invalid parameters"}

        instance_cart = http.request.env["ecom_espadas.cart"]
        cart = instance_cart.get_or_create_cart()
        cart.remove_product(product_id)
        return {"status": "success"}

    @http.route("/api/cart/checkout", type="json", auth="public", website=True)
    def checkout(self):
        instance_cart = http.request.env["ecom_espadas.cart"]
        cart = instance_cart.get_or_create_cart()

        if not cart.line_ids:
            return {"status": "failure", "message": "Cart is empty"}

        order_id = cart.checkout()
        return {"status": "success", "order_id": order_id}

    @http.route("/api/product/create", type="json", auth="public", website=True)
    def create_product(self):
        json_data = http.request.jsonrequest
        name = json_data.get("name")
        price = json_data.get("price")
        stock = json_data.get("stock")

        if not all([name, price, stock]):
            return {"status": "failure", "message": "All fields are required"}

        product = http.request.env["ecom_espadas.product"].create(
            {"name": name, "price": price, "stock": stock}
        )
        return {"status": "success", "product_id": product.id}

    @http.route("/api/product/create", type="json", auth="public", website=True)
    def create_product(self):
        json_data = http.request.jsonrequest
        name = json_data.get("name")
        price = json_data.get("price")
        stock_quantity = json_data.get("stock_quantity")

        if not all([name, price, stock_quantity]):
            return {"status": "failure", "message": "All fields are required"}

        product = http.request.env["ecom_espadas.product"].create(
            {"name": name, "price": price, "stock_quantity": stock_quantity}
        )
        return {"status": "success", "product_id": product.id}
