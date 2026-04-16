import json
my_dict = {
    'Software': 'Python',
    'version': '3.12.1',
    'Days coding': 143,
    'proficiency': 'Noob',
    'Dream Job': 'Junior developer'
}

print(my_dict)
print(type(my_dict))

my_dict_json = json.dumps(my_dict, indent=2)

file = open('test.txt', 'w')
file.write(my_dict_json)
