# *args in Functions - allows variable number of positional arguments

# Example 1: Understanding *args basics
#def sort_nums(*args):
   # print(args)            # Prints tuple of all arguments
   # print(type(args))      # <class 'tuple'>

   # for arg in args:
        #print(arg)          # Iterate through each argument


#sort_nums(10, 3 ,15, 246, 23)
# *args gathers all positional arguments into a tuple
# Tuples are ordered and immutable

# args.append() will give error because tuples are immutable
# We are using positional arguments (no keyword=value)

# Can also do *(parameter) when calling function to unpack a sequence


# Example 2: Using *args to create flexible functions

#def sort_nums(*args):
    #return sorted(args)   # sorted() returns a list from the tuple

#sorted_nums = sort_nums(10,3,15,246,23)
#print(sorted_nums)

# Example 3: Calling function multiple times with different number of arguments
def sort_nums(*args):
    # *args collects all positional arguments into a tuple
    # sorted() converts tuple to sorted list
    return sorted(args)

# First call with 5 arguments
sorted_nums = sort_nums(10,3,15,246,23)
print(sorted_nums)  # [3, 10, 15, 23, 246]

# Can call function with different number of arguments - this is the power of *args!
sorted_nums = sort_nums(5,432,232,21,443,3)
print(sorted_nums)  # [3, 5, 21, 232, 432, 443]

# Append to the list returned by the function (not the args tuple)
sorted_nums.append(20)
print(sorted_nums)  # Appends to the last assigned sorted_nums list only