my_motorbike = {
    'brand': 'Ducati',
    'price': 25000,
    'engine_vol':1.2,
}
print(len(my_motorbike))
del my_motorbike['brand']
print(len(my_motorbike))

#get method, to see if the key exists in dictionary
print(my_motorbike.get('brand'))
print(my_motorbike.get('price'))
print(my_motorbike.get('qty', 0))

#output is not the same as Bogdan's, we deleted the key-value pair 'brand':'Ducati'
# dictionary - The __doc__ method

my_dict ={}
print(my_dict.__doc__)
