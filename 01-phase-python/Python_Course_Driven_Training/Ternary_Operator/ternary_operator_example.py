#first example

my_number = 21
print("it's an integer") if type(my_number) is int else print("it's not an integer")

#or we can do
if type(my_number) is int:
    print("it's an integer")
else:
    print("it's not an integer")

# second example
product_qty = 10
print("in stock" if product_qty > 0 else "out of stock")

# third example
temp = +24
weather = "hot" if temp > 20  else "cold"
print(weather)