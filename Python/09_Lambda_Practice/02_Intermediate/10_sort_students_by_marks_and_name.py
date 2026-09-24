students = [
    ("Ravi", 85),
    ("Asha", 92),
    ("Neha", 85),
    ("Aman", 92)
]

students.sort(key=lambda x: (-x[1], x[0]))

print(students)
