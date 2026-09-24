marks = [95, 82, 67, 54, 90]

res = []

for mark in marks:

    if mark >= 90:
        res.append("A")

    elif mark >= 75:
        res.append("B")

    elif mark >= 60:
        res.append("C")

    else:
        res.append("D")

print(res)