import re

my_text = "This   is a   very  long      not formatted   sentence"
print(my_text)
regexp = r'\s+'

words = re.split(regexp, my_text)
print(words)
print(' '.join(words))

print(my_text.split(' '))