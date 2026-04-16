# Task: Create a dictionary by getting user input for 3 key-value pairs

# Initialize an empty dictionary to store user input
user_dict = {}

# Get first key-value pair from user
key1 = input("Enter the name of the first key:")
value1 = input("Enter the value for this key:")
# Add the key-value pair to the dictionary using bracket notation
user_dict[key1] = value1

# Get second key-value pair from user
key2 = input("Enter the name of the second key:")
value2 = input("Enter the value for this key:")
# Add second pair to dictionary
user_dict[key2] = value2

# Get third key-value pair from user
key3 = input("Enter the name of the third key:")
value3 = input("Enter the value for this key:")
# Add third pair to dictionary
user_dict[key3] = value3

# Show results
print("\nFinal dictionary:")
print(user_dict)

# Go over this again, this relied on input, need 3 name, 3 values, so need to repeat sequence 3 times
# Can use loop - wait to learn about loops and how they can be applied to this exercise

# Alternative solution (more concise prompts):
# Initialize another empty dictionary
user_dict = {}

# Collect first key-value pair with shorter prompts
key1 = input("Key 1: ")
value1 = input("Value 1: ")
user_dict[key1] = value1

# Collect second key-value pair
key2 = input("Key 2: ")
value2 = input("Value 2: ")
user_dict[key2] = value2

# Collect third key-value pair
key3 = input("Key 3: ")
value3 = input("Value 3: ")
user_dict[key3] = value3

# Display the final dictionary
print(user_dict)