import re

regexp = r'bad'

my_text = "Something bad is here. bad situation. bad words"

changed_text = re.sub(regexp, '*', my_text)
print(changed_text)
