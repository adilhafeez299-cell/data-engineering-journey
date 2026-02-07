import re

my_string = 'my name is Adil'

res = re.search('Adil', my_string)
print(res)
print(type(res))