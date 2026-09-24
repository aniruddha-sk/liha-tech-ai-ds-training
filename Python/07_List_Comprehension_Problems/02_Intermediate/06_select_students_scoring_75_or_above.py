students = [
    ('Asha', 82),
    ('Ravi', 68),
    ('Neha', 91),
    ('Aman', 75)
]

res = [name for name, score in students if score >= 75]

print(res)