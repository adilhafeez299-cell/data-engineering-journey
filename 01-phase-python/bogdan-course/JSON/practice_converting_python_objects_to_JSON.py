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

my_fave_song_json = json.dumps(my_fave_song)
print(my_fave_song_json)
print(type(my_fave_song_json))