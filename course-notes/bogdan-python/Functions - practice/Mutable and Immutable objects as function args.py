#def print_fruits_info(person_name, fruits):
   # print(person_name, fruits)

#my_name = 'Adil'
#favorite_fruits = ['oranges', 'apples', 'bananas']

#print_fruits_info(my_name, favorite_fruits)


# example 2

#def print_fruits_info(person_name, fruits):
    # for fruit in fruits:
    #     print(f'{person_name} likes {fruit}')

#my_name = 'Adil'
#favorite_fruits = ['oranges', 'apples', 'bananas']

#(my_name, favorite_fruits)

# example 3, create copies if immutable objects
def print_fruits_info(person_name, fruits):
    fruits_copy = fruits.copy()
    fruits_copy.pop()
    for fruit in fruits_copy:
        print(f'{person_name} likes {fruit}')

my_name = 'Adil'
favorite_fruits = ['oranges', 'apples', 'bananas']
print_fruits_info(my_name, favorite_fruits)


print(favorite_fruits) # did not modify external variable inside the Function
# if we are not modifying insideFunction we don't need to create copy of mutable object


