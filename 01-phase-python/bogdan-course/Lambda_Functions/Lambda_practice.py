students = [
    {'name': 'john', 'score': 50},
    {'name': 'Alice', 'score': 20},
    {'name': 'Bob', 'score': 90}
]

#def sort_by_score(x):
   # return x['score']

students.sort(key=lambda student: student['score'], reverse=True)
print(students)