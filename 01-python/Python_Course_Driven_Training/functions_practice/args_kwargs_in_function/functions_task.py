# Task: Create a merge_lists_to_dict function
# - The function must have two parameters
# - The function should combine two lists using the built-in zip function
# - Convert a zip object to a dictionary and return it from the function
# - Call a function by passing it two lists as arguments
# - Output the results of the function call to the terminal

# Define function that takes two lists and merges them into a dictionary
def merge_lists_to_dict(list1, list2):
    # zip() pairs elements from both lists: (list1[0], list2[0]), (list1[1], list2[1]), etc.
    # dict() converts those pairs into key-value pairs
    return dict(zip(list1,list2))

# Create two lists - one for keys, one for values
l1 = ['Name', 'Age', 'sex', 'city']
l2 = ['Adil', 25, 'Male', 'London']

# Call the function and print the resulting dictionary
print(merge_lists_to_dict(l1, l2))  # {'Name': 'Adil', 'Age': 25, 'sex': 'Male', 'city': 'London'}
