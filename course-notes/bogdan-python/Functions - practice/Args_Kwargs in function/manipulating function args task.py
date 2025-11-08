def merge_lists_to_dict(list_1, list2):
    return dict(zip(list_1, list2))


result1 = merge_lists_to_dict(list_1=[1, 2, 3], list2=['a', 'b', 'c'])
print(result1)

result2 = merge_lists_to_dict([1, 2, 3], list2=['a', 'b', 'c'])
print(result2)


# with positional argument, keyword argument

# using *args and **kwargs

# *args
def merge_lists_to_dict_args(*args):
    return dict(zip(args[0], args[1]))


result3 = merge_lists_to_dict_args([1, 2, 3], ['a', 'b', 'c'])
print(result3)


# **kwargs
def merge_lists_to_dict_kwargs(**kwargs):
    return dict(zip(kwargs['list_1'], kwargs['list2']))


result4 = merge_lists_to_dict_kwargs(list_1=[1, 2, 3], list2=['a', 'b', 'c'])
print(result4)

# need to go over again as I was definitely a bit confused!!
