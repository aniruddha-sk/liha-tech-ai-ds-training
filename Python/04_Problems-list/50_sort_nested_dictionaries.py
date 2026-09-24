students = [
    {"name": "Amit", "age": 25},
    {"name": "Rahul", "age": 20},
    {"name": "Sneha", "age": 23}
]

students.sort(key=lambda x: x["age"])

print(students)