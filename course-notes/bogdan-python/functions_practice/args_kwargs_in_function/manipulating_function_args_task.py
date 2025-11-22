# Task: Manipulating function arguments - comparing different approaches

# Approach 1: Standard named parameters
def merge_lists_to_dict(list_1, list2):
    # Zip pairs elements from both lists and convert to dictionary
    return dict(zip(list_1, list2))

# Call with keyword arguments (explicit parameter names)
result1 = merge_lists_to_dict(list_1=[1, 2, 3], list2=['a', 'b', 'c'])
print(result1)  # {1: 'a', 2: 'b', 3: 'c'}

# Call with mixed positional and keyword arguments
result2 = merge_lists_to_dict([1, 2, 3], list2=['a', 'b', 'c'])
print(result2)  # {1: 'a', 2: 'b', 3: 'c'}


# Comparing approaches: positional vs keyword arguments

# Approach 2: Using *args (positional arguments gathered into tuple)
def merge_lists_to_dict_args(*args):
    # Access arguments by index: args[0] is first list, args[1] is second list
    return dict(zip(args[0], args[1]))

# Must call with positional arguments only (no keyword names)
result3 = merge_lists_to_dict_args([1, 2, 3], ['a', 'b', 'c'])
print(result3)  # {1: 'a', 2: 'b', 3: 'c'}


# Approach 3: Using **kwargs (keyword arguments gathered into dictionary)
def merge_lists_to_dict_kwargs(**kwargs):
    # Access arguments by key name from the kwargs dictionary
    return dict(zip(kwargs['list_1'], kwargs['list2']))

# Must call with keyword arguments (key=value syntax)
result4 = merge_lists_to_dict_kwargs(list_1=[1, 2, 3], list2=['a', 'b', 'c'])
print(result4)  # {1: 'a', 2: 'b', 3: 'c'}

# Need to go over again as I was definitely a bit confused!!

# Task 2: Create an update_car_info function
# - All named arguments will be combined into a car dictionary
# - Add a new is_available key to the dictionary with value True
# - Return modified dictionary from the function
def update_car_info(**kwargs):
    # kwargs already is a dictionary containing all keyword arguments
    car_info = kwargs
    # Add new key-value pair to the dictionary
    car_info['is_available'] = True
    return car_info

# Call function with various car attributes as keyword arguments
car = update_car_info(brand = 'Toyota', model = 'Camry', year = 2020)
print(car)  # {'brand': 'Toyota', 'model': 'Camry', 'year': 2020, 'is_available': True}