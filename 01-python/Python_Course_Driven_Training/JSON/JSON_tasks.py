import json
from datetime import datetime


sick_dict = {
    'Fave_Anime': 'JiJitsu Kaisen',
    'Rating': 10,
    'Time right now': '14:36',
    'Gender is Male': True,
    'Things to do today': ['Gym', 'Run', 'Eat']
}

sick_dict_json = json.dumps(sick_dict)
print(sick_dict_json)
print(type(sick_dict_json))

# Task 2

dict_list = [
    {
      'favorite_snack': 'Sharwarma',
      'Spice level':  'Extra Hot',
      'Rating': 10,
      'ingredients': ['Lamb','Tahini','pickles','lebanese bread','tomatoes','onion','Garlic Sauce','Extra Chilli'],
      'tasty' : True
    },
    {
            'Movie': 'Avatar: Fire and Ash',
            'Seeing with Friend': True,
            'Are you excited': 'yes',
            # Automatically get today's date in YYYY-MM-DD format
            'Date': datetime.now().strftime("%Y-%m-%d")
     },
    {
        'session_name': 'Upper Body Push',
        'intensity_level': 'High',
        'duration_minutes': 60,
        'exercises': [
            {'name': 'Bench Press', 'sets': 4, 'reps': 8},
            {'name': 'Shoulder Press', 'sets': 3, 'reps': 12},
            {'name': 'Tricep Dips', 'sets': 3, 'reps': 15}
        ],
        'completed': False
    }
]

my_dict_list_json = json.dumps(dict_list, indent=2)
print(my_dict_list_json)

json.loads(my_dict_list_json)
print(json.loads(my_dict_list_json))

print(dict_list == json.loads(my_dict_list_json))
print(type(dict_list))
print(type(my_dict_list_json))