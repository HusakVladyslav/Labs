def calculate_total_price(order_items):
    total_price = 0
    for item in order_items:
        item_price = item['price']
        item_quantity = item['quantity']
        total_price += item_price * item_quantity
    return total_price

def apply_discount(total_price):
    if total_price > 1000:
        discount = 0.1
    elif total_price > 500:
        discount = 0.05
    else:
        discount = 0
    return discount

def calculate_shipping_cost(total_price_after_discount):
    if total_price_after_discount > 100:
        shipping_cost = 0
    else:
        shipping_cost = 10
    return shipping_cost

def process_orders(orders):
    processed_orders = []
    for order in orders:
        customer_name = order['customer_name']
        order_items = order['order_items']
        total_price = calculate_total_price(order_items)
        discount = apply_discount(total_price)
        total_price_after_discount = total_price * (1 - discount)
        shipping_cost = calculate_shipping_cost(total_price_after_discount)
        order_details = {
            'customer_name': customer_name,
            'total_price': total_price,
            'discount': discount,
            'total_price_after_discount': total_price_after_discount,
            'shipping_cost': shipping_cost,
            'order_items': order_items
        }
        processed_orders.append(order_details)
    return processed_orders