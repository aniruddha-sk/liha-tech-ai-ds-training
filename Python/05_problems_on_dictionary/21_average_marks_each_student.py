students = {
    "Amit": {"Python": 80, "ML": 90},
    "Neha": {"Python": 92, "ML": 88}
}

for name, subjects in students.items():
    total = 0

    for mark in subjects.values():
        total = total + mark

    average = total / len(subjects)

    print(name, "=", average)