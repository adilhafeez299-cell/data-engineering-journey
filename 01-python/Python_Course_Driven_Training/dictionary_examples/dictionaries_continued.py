# Other operations with dictionaries - Nested dictionaries example

# Create a dictionary with nested dictionary structure
# Outer dictionary contains motorbike properties
my_motorbike = {
    'brand':'Ducati',
    'engin_vol':'1.2',
    # Nested dictionary for price-related information
    'price_info': {
        'price':'25000',
        'is_available':'true',
    }
}
# Access nested dictionary value using chained bracket notation
# First key 'price_info' accesses the nested dict, second key 'price' gets the value
print(my_motorbike['price_info']['price'])
#25000
# Access another nested value from the price_info dictionary
print(my_motorbike['price_info']['is_available'])
#true

