#other operations with dictionaries

my_motorbike = {
    'brand':'Ducati',
    'engin_vol':'1.2',
    'price_info': {
        'price':'25000',
        'is_available':'true',
    }
}
print(my_motorbike['price_info']['price'])
#25000
print(my_motorbike['price_info']['is_available'])
#true

