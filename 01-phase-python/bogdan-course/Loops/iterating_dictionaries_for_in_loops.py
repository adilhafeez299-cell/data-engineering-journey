product_prices = {
    'PC':1000,
    'Mobile Phone': 200,
    'Tablet': 500,
    'Laptop': 1500,
    'Headphones': 100,
    'Camera': 2000,
    'Accessories': 50,
    'Other': 'Free'
}

print(type(product_prices.items()))

for item in product_prices.items():
    device, price = item
    print(device, price)
