students = {
    "Amit": {
        "Python": 90,
        "ML": 85
    },
    "Neha": {
        "Python": 88,
        "ML": 94
    }
}

for student, subjects in students.items():

    highest_subject = max(subjects, key=subjects.get)
    highest_marks = subjects[highest_subject]

    print(student, "->", highest_subject, "(", highest_marks, ")")