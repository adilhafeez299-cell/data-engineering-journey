from unittest import result


def dict_to_list(dictionary):
    for key, value in dictionary.items():
        if isinstance(value, int):
            print(value*2)


dict_to_list({'a': 1, 'b': 2})

def dict_to_list(dictionary):
    result = []
    for key, value in dictionary.items():
        if isinstance(value, int):
            result.append((key, value * 2))
        else:
            result.append(value)
    return result

output = dict_to_list({'a': 1, 'b': 2})
print(output)



def filter_list(list_sequence, value_type):
    result = []
    for item in list_sequence:
        if isinstance(item, value_type):
            result.append(item)
    return result

print(filter_list([1, 2, 3, 'a', 'b'], int))