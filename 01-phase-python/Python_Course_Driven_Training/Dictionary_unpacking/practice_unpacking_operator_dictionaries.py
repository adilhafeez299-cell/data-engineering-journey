person = {'name':'john', 'age':25 }

#other_person = person.copy()
#other_person['age'] = 30

other_person = {
**person, 'age':30
}

print(person)
print(other_person)
# first have to unpack keys from person dictionary, then add new age, will not work other way round
