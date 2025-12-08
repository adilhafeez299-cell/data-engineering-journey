#Assigning Values from the list to variables
#my_apple = my_fruits[0]
#my_lime = my_fruits[2]

#print(my_apple)
#print(my_banana)
#print(my_lime)

# can unpack the following way

my_fruits = ['apple', 'banana', 'lime']
my_apple, my_banana, my_lime = my_fruits

print(my_apple)
print(my_banana)
print(my_lime)

# can do the same for tuple
my_fruits2 = ('apple2', 'banana2', 'lime2')
print(type(my_fruits2))
my_apple2, my_banana2, my_lime2 = my_fruits2
print(my_apple2)
print(my_banana2)
print(my_lime2)

my_fruits3 = ('apple3', 'banana3', 'lime3')
print(my_fruits3)
my_apple3, *my_other_fruits3 = my_fruits3
print(type(my_other_fruits3))
print(my_apple3)
print(my_other_fruits3)

# unpacking the dictionary into keyword arguments example
user_profile = {
    'name': 'adil',
    'comments_qty': 23,
}

def user_info(name, comments_qty=0):
    if not comments_qty:
        return f"{name}' has no {comments_qty} comments"

    return f"{name} has {comments_qty} comments"

print(user_info(**user_profile))

# unpacking the list into positional arguments example
user_data = ['adil', 23]
def user_info2(name, comments_qty):
    if not comments_qty:
        return f"{name}' has no {comments_qty} comments"
    return f"{name} has {comments_qty} comments"

print(user_info2(*user_data))
