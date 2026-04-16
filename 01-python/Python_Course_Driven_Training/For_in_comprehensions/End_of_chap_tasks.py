#Workout_dict = {
    #'Bench': '270lbs',
    #'Shoulder Press': '180lbs',
   # 'Trice pushdown': '150lbs'
#}

#new_workout_dict = {k: v.upper() for k, v in Workout_dict.items()}
#print(new_workout_dict)

# Create a dictionary with your exercises and weight lifted
gym_dict = {
    'Bench': 270,
    'Deadlift': 400,
    'Squat': 350
}
new_workout_dict_2 = {k: v + 20 for k, v in gym_dict.items()}
print(new_workout_dict_2)

# task 2

hobbies = ['running', 'swimming', 'gaming', 'cinema', 'coding']
filtered = [hobby for hobby in hobbies if len(hobby) > 5]
filtered.reverse()
print(filtered)




