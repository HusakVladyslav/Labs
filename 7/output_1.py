class Product:
    def __init__(self, product_id, name, category, price):
        self._product_id = product_id
        self._name = name
        self._category = category
        self._price = price

    @property
    def product_id(self):
        return self._product_id

    @property
    def name(self):
        return self._name

    @property
    def category(self):
        return self._category

    @property
    def price(self):
        return self._price


class InventoryManagement:
    def __init__(self, products):
        self.products = products

    def print_product_details(self, product_id):
        for product in self.products:
            if product.product_id == product_id:
                print(f"Product ID: {product.product_id}, Name: {product.name}, Category: {product.category}, Price: {product.price}")