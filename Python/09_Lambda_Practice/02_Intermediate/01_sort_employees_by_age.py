employees = [
    {"name": "Asha", "age": 29},
    {"name": "Ravi", "age": 24},
    {"name": "Neha", "age": 31}
]

employees.sort(key=lambda x: x["age"])

print([x["name"] for x in employees])
