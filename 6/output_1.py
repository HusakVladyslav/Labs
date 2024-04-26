def calculate_total_price(product_prices, discount, tax_rate=0):
    total_price = 0
    for price in product_prices:
        if discount:
            price *= 0.9  # 10% знижка
        total_price += price
    total_price *= (1 + tax_rate)
    return total_price

# Приклад без налогів
product_prices_without_tax = [100, 200, 300]
discount_applied = True  # Знижка застосовується

total_price_without_tax = calculate_total_price(product_prices_without_tax, discount_applied)
print("Total price without tax:", total_price_without_tax)

# Приклад з налогами (8% податок)
tax_rate = 0.08
total_price_with_tax = calculate_total_price(product_prices_without_tax, discount_applied, tax_rate)
print("Total price with tax:", total_price_with_tax)