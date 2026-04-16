person = ('Bob', 25)

name, age, *other = person

print(name)
print(age)
print(other)

school_grades = (80, 75,35, 20, 90)
first, *middle, last = school_grades
print(first)
print(middle)
print(last)


school_grades = (80, 75,35, 20, 90)
first, second, *remaining = school_grades
print(first)
print(middle)
print(last)

