students = [
    {"name": "Amit", "age": 21, "city": "Pune"},
    {"name": "Rahul", "age": 22, "city": "Mumbai"}
]

for student in students:
    del student["age"]

print(students)