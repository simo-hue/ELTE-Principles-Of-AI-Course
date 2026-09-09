students = [
    {'name': 'Alice', 'grade': 85},
    {'name': 'Bob', 'grade': 92},
    {'name': 'Charlie', 'grade': 78}
]

# or using bracket notation: key=lambda student: student['grade']
sorted_students = sorted(students, key=lambda student: student.get('grade'), reverse=True)

print(sorted_students)