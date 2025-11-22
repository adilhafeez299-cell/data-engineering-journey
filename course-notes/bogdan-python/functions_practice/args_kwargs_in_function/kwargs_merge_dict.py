# **kwargs - Merging keyword arguments into a dictionary

# Example 1: Standard function with named parameters
#def product_price_info(product_title, product_price):
    #print(f'{product_title} costs {product_price}$')

#product_price_info(product_title= "Bottle of water", product_price = 2)

# Example 2: Using **kwargs - can accept any number of keyword arguments
#def product_price_info(**product):
    # **product gathers all keyword arguments into a dictionary
    #print(f"{product['product_title']} costs {product['product_price']}$")

#product_price_info(product_title= "Bottle of water", product_price = 2, product_availability = True)
# Can pass extra keyword arguments that weren't explicitly defined!

# Example 3: Extracting values from **kwargs dictionary
def product_price_info(**product):
    # Extract specific values from the dictionary
    title = product['product_title']
    price = product['product_price']
    print(f'{title} costs {price} $')

# Call function with keyword arguments
product_price_info(product_title = 'bottle of water', product_price = 2)

# Keyword arguments are gathered into a single dictionary (the **product parameter)
