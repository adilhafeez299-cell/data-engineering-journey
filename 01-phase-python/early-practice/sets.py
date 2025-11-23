# Create a set (unordered collection of unique elements)
set1 = {1, 2, 3, 4, 5}
# Add element 6 to set1
set1.add(6)  # set1 is now {1, 2, 3, 4, 5, 6}

# Create a second set
set2 = {4,5,6,7,8}

# Find common elements between both sets using intersection
common = set1.intersection(set2)  # Returns {4, 5, 6}
# Convert the resulting set to a list
common_list = list(common)
# Print the common elements as a list
print(common_list)
# Print the type to confirm it's a list
print(type(common_list))  # <class 'list'>