# Create a dictionary with motorbike details
my_motorbike = {
    'brand': 'Ducati',
    'price': 25000,
    'engine_vol':1.2,
}
# Print the number of key-value pairs in the dictionary
print(len(my_motorbike))  # Output: 3
# Delete the 'brand' key-value pair from the dictionary
del my_motorbike['brand']
# Print the updated length after deletion
print(len(my_motorbike))  # Output: 2

# get method - safely access dictionary values (returns None if key doesn't exist)
# Try to get 'brand' key (will return None since we deleted it)
print(my_motorbike.get('brand'))  # Output: None
# Get 'price' key value (exists in dictionary)
print(my_motorbike.get('price'))  # Output: 25000
# Get 'qty' key with default value 0 if key doesn't exist
print(my_motorbike.get('qty', 0))  # Output: 0 (key doesn't exist, returns default)

# Output is not the same as Bogdan's, we deleted the key-value pair 'brand':'Ducati'
# Dictionary - The __doc__ method (displays documentation for dict class)

# Create an empty dictionary
my_dict ={}
# Print the built-in documentation string for dictionary objects
print(my_dict.__doc__)
