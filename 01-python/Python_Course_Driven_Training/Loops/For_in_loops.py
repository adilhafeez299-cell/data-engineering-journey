#For in for list
my_list = [True, 10, 'abc', {}]

for elem in my_list:
    print(elem)

#For in for tuple
video_info = ('1920x1080', True, 27)

for elem in video_info:
    print(elem)

#For in for dictionary
contact_information = {
    'email': 'Adil.1@gov.com',
    'number': 2122122300,
    'Address': 'Dhaka',
    'is_alive': True
}

for key in contact_information:
    print( key, contact_information[key])

# For in for dictionaries and items() method
my_object = {
    'x': 10,
    'y' : True
}
for item in my_object.items():
    print(item)

my_object = {
    'x1': 23,
    'y1': False
}
for item in my_object.items():
    key, value = item
    print(key, value)
   # print(type(key), type(value))

#can also do

for key, value in my_object.items():
    print(key, value)


#For in for sets

video_ids = {'123', '456', '789'}
for id in video_ids:
    print(id)

#For in for string
for char in 'hello':
    print(char)

#For in for range
for num in range(10):
    print(num)

for odd_num in range(3,10,2):
    print(odd_num)