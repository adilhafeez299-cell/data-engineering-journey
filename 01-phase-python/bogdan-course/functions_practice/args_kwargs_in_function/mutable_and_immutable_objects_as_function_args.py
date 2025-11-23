# Example 1: Simple function that prints mutable list argument
#def print_fruits_info(person_name, fruits):
   # print(person_name, fruits)  # Just prints the list directly

#my_name = 'Adil'
#favorite_fruits = ['oranges', 'apples', 'bananas']  # Mutable list

#print_fruits_info(my_name, favorite_fruits)


# Example 2: Function that iterates through the mutable list

#def print_fruits_info(person_name, fruits):
    # for fruit in fruits:
    #     print(f'{person_name} likes {fruit}')  # Loop through list

#my_name = 'Adil'
#favorite_fruits = ['oranges', 'apples', 'bananas']

#(my_name, favorite_fruits)

# Example 3: Create copies of mutable objects to avoid modifying the original
# This demonstrates how to safely work with mutable objects in functions
def print_fruits_info(person_name, fruits):
    # Create a shallow copy of the fruits list to avoid modifying the original
    fruits_copy = fruits.copy()
    # Remove the last element from the COPY only
    fruits_copy.pop()
    # Iterate through the copied (and modified) list
    for fruit in fruits_copy:
        print(f'{person_name} likes {fruit}')

# Define variables
my_name = 'Adil'
favorite_fruits = ['oranges', 'apples', 'bananas']
# Call function with the original list
print_fruits_info(my_name, favorite_fruits)

# Verify the original list was NOT modified
print(favorite_fruits) # Did not modify external variable inside the Function
# If we are not modifying inside Function we don't need to create copy of mutable object


