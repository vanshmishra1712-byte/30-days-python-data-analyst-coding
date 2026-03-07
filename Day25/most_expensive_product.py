# Q25: Find the most expensive product from a dictionary

products = {
    "Laptop": 75000,
    "Phone": 40000,
    "Tablet": 30000,
    "Monitor": 20000
}

max_price = 0
expensive_product = ""

for product in products:
    if products[product] > max_price:
        max_price = products[product]
        expensive_product = product

print(expensive_product)
print(max_price)