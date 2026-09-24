students = [
    {"name": "Asha", "score": 82},
    {"name": "Ravi", "score": 74},
    {"name": "Neha", "score": 91}
]

def get_score(student):
    return student["score"]

students.sort(key=get_score)

print([student["name"] for student in students])
