# Using variables with dictionaries - demonstrating dynamic value assignment

# Define variables to store motorbike attributes
brand = 'Ducati'
bike_price = 25000
engine_vol = 1.2

# Create dictionary using variables as values (not keys)
# This allows you to use pre-defined values in dictionary creation
my_motorbike = {
    'price': bike_price,        # Value comes from bike_price variable
    'engine_vol': engine_vol    # Value comes from engine_vol variable
}
