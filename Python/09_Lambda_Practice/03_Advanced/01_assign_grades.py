marks = [95, 81, 69, 52]

grade = lambda x: "A" if x >= 90 else "B" if x >= 75 else "C" if x >= 60 else "D"

result = list(map(grade, marks))

print(result)
