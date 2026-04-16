from array import array

# create an integer array (all values must be ints)
my_int_array = array('i', [10, 4, 3, 7, 9])

print(my_int_array)
print(type(my_int_array))
print(dir(my_int_array))

# access element
print(my_int_array[2])

# append an integer
my_int_array.append(20)
print(my_int_array)

# appending a float would raise a TypeError
# my_int_array.append(10.5)

# appending True works because bool is a subclass of int (True == 1)
my_int_array.append(True)
print(my_int_array)

# type checks
print(isinstance(True, bool))  # True
print(isinstance(True, int))   # True

# show int subclasses (includes bool)
print(int.__subclasses__())