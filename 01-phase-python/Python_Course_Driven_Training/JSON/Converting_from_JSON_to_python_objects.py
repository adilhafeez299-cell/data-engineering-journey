import json

my_nums = [10, 100, 5, 20]

my_nums_json = json.dumps(my_nums)
print(type(my_nums_json))
print(my_nums_json)

my_nums.extend(([3,4]))
print(my_nums)
print(my_nums_json)


my_fave_song = {
    'title': "Way down we go",
    'description': 'Favorite gym track',
    'tags': ['fave', 'sick', 'kewl'],
    'rating': 9,
    'year':2012,
    'times played': 'over 9000'
}

print(my_fave_song)
print(my_fave_song['title'])
print(my_fave_song['description'])
print(my_fave_song['tags'])
print(my_fave_song['rating'])
print(my_fave_song['year'])
print(my_fave_song['times played'])

# dict -> JSON
my_fave_song_json = json.dumps(my_fave_song)
print(my_fave_song_json)
print(type(my_fave_song_json))

#JSON -> dict
my_fave_song = json.loads(my_fave_song_json)
print(my_fave_song)
print(type(my_fave_song))

# dict with function ## this is redundant code

#def sum_fn(a, b):
    #return a + b

#my_math = {
    #'#title': "Math dict",
    #'sum': sum_fn
#}

#my_math_json = json.dumps(my_math)
#print(my_math_json)

#JSON -> list
my_list = json.loads('[10, "abc", null, []]')
print(my_list)


