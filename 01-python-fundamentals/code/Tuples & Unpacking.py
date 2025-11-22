# Create a tuple (immutable sequence)
info = ("Adil", 26, "London")
print("Original:", info)

# Tuple unpacking - assign each element to a separate variable
name, age, city = info
print(name)   # "Adil"
print(age)    # 26
print(city)   # "London"

# Convert tuple to list (since tuples are immutable and can't be modified directly)
info_list = list(info)
# Modify the list element at index 2
info_list[2] = "Dubai"
# Convert the list back to a tuple
info = tuple(info_list)
# Compare values (True if values are same)
print(info == info_list)      # False (different types: tuple vs list)
# Compare memory addresses (will be False - different objects)
print(id(info) == id(info_list))

# Print the updated tuple
print("Updated:", info)