def calculate_school_grade(percentage_data):
    return 'pass' if percentage_data >= 50 else 'fail'

percentage = 70
grade = calculate_school_grade(percentage)
print(grade)

# this is my example
# bogdan example

def get_letter_grade(score):
   letter_grade =  'A' if score >= 90 else 'B' if score >= 80 else 'C' if score >= 70 else 'D' if score >= 60 else 'F'
   return letter_grade

print(get_letter_grade(83))
print(get_letter_grade(25))
print(get_letter_grade(100))


