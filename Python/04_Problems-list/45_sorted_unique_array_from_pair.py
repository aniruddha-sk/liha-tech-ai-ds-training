numbers = [5, 2, 8, 2, 5, 1, 8]

unique = []

for number in numbers:
    if number not in unique:
        unique.append(number)

unique.sort()

print(unique)