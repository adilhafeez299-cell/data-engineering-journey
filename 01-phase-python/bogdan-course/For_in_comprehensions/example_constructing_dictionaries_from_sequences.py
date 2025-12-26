grades = (80, 95, 65)
subjects = ['Science', 'Math', 'English']

grade_dict = {subject: grade - 10 for subject, grade in zip (subjects, grades)}
print(grade_dict)