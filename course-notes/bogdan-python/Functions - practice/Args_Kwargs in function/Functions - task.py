# Create a merge_lists_to_dict function
# the function must have two parameters
# the function should combine two lists using the built-in zip fuction
#convert a zip object to a dictionary and return it from the function
# call a function by passing it two lists as arguments
# output the results of the function call to the terminal

def merge_lists_to_dict(list1, list2):
    return dict(zip(list1,list2))

l1 = ['Name', 'Age', 'sex', 'city']
l2 = ['Adil', 25, 'Male', 'London']

print(merge_lists_to_dict(l1, l2))
