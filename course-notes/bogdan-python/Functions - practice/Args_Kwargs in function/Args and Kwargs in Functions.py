# Example 1:
#def sort_nums(*args):
   # print(args)
   # print(type(args))

   # for arg in args:
        #print(arg)


#sort_nums(10, 3 ,15, 246, 23)
# sorts arguments into tuple
#tuples are ordered/ immutable

# args.append will give error
# we are using positional arguments

# can also do *(parameter)


# Example 2:

#def sort_nums(*args):
    #return sorted(args)

#sorted_nums = sort_nums(10,3,15,246,23)
#print(sorted_nums)

def sort_nums(*args):
    return sorted(args)

sorted_nums = sort_nums(10,3,15,246,23)
print(sorted_nums)
# can call function with different arguments
sorted_nums = sort_nums(5,432,232,21,443,3)
print(sorted_nums)
sorted_nums.append(20)
print(sorted_nums)
# only append last list