person = {
    'name': 'Adil',
    'favorite_number': 23,
    'is_alive': True,
    'job': ('Software Engineer')
}

person_str_values = [value for value in person.values() if type(value) == str]
print(person_str_values)