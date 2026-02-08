import re

my_string = 'My name is Adil.'
res_2 = re.search(r'^M.*Adil\.$', my_string)
print(res_2)


## creating patterns
#use pattern object to create different matches

my_pattern = re.compile(r'B....n')
print(my_pattern)
print(type(my_pattern))


print(my_pattern.search(my_string))
print(my_pattern.search("Hello, this is Boooon"))

print(my_pattern.match(my_string))
print(my_pattern.match('Boooon'))
print(my_pattern.match('Bogdan!!!'))

print(my_pattern.findall("My name is Bogdan. Hello Bogdan"))