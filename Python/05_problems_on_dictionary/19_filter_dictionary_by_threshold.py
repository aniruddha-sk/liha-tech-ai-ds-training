marks = {"Amit": 75, "Neha": 91, "Ravi": 84}

threshold = 80

result = {}

for name, mark in marks.items():
    if mark >= threshold:
        result[name] = mark

print(result)