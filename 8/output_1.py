class Address:
    def __init__(self, address):
        self.address = address

    def is_in_new_york(self):
        return "New York" in self.address

    def is_in_california(self):
        return "California" in self.address

class Customer:
    def __init__(self, name, address):
        self.name = name
        self.address = Address(address)

class Order:
    def __init__(self, customer, product, quantity):
        self.customer = customer
        self.product = product
        self.quantity = quantity

    def print_order_details(self):
        print(f"Order for {self.product} x {self.quantity}")
        print(f"Shipping to {self.customer.address.address}")

    def calculate_shipping_cost(self):
        if self.customer.address.is_in_new_york():
            return 5.00
        elif self.customer.address.is_in_california():
            return 10.00
        else:
            return 15.00