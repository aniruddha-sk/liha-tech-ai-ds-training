students = [
    ("Asha", 82),
    ("Ravi", 68),
    ("Neha", 91),
    ("Aman", 75)
]

result = list(filter(lambda x: x[1] >= 75, students))

print(result)
