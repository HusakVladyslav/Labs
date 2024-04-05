class ProductSearch:
    def search_product(self, products, query):
        # Пошук товару за запитом
        pass

class ProductDisplay:
    def display_product(self, product):
        # Відображення інформації про товар
        pass

class ProductOrder:
    def order_product(self, product, quantity):
        # Замовлення товару
        pass

class Product:
    def __init__(self, name, price, type):
        self.name = name
        self.price = price
        self.type = type