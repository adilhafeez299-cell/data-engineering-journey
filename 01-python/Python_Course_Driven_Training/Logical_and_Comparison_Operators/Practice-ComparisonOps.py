# comparison operators examples
a = [1, 2]
b = [1, 2]


print(id(a))
print(id(b))


print(a > b)
# a.__gt__(b)
print(a >= b)
# a.__ge__(b)
print(a < b)
# a.__lt__(b)
print(a <= b)
# a.__le__(b)
print(a == b)
#a.__eq__(b)
print(a != b)
#a.__ne__(b)


# can compare different sequences in python


name = 'Alice'
if len(name) > 4:
    print("Name is longer than 4 characters")

my_nums = (10, 3, 20, 6)
if sum(my_nums) > 20:
    print("Sum of numbers is greater than 20")


if my_nums == sorted(my_nums):
    print("Numbers are sorted")

other_nums = [3.5, 4.6, 7.7, 8.9, 10]
if other_nums == sorted(other_nums):
    print("Numbers are sorted")

# del statement deletes a variable
# example

my_dict = {'a': True, 'b':10}
del my_dict['a']
my_dict.__delitem__('b')
print(my_dict)
print(my_dict.__delitem__)