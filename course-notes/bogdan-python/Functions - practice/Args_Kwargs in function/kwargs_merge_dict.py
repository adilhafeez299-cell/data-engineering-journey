#def product_price_info(product_title, product_price):
    #print(f'{product_title} costs {product_price}$')

#product_price_info(product_title= "Bottle of water", product_price = 2)

#def product_price_info(**product):

    #print(f"{product['product_title']} costs {product['product_price']}$")

#product_price_info(product_title= "Bottle of water", product_price = 2, product_availability = True)

def product_price_info(**product):
    title = product['product_title']
    price = product['product_price']
    print(f'{title} costs {price} $')

product_price_info(product_title = 'bottle of water', product_price = 2)

#keyword arguments are gathered into a single dictionary
