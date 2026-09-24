numbers = [1, 2, 3]

sublists = []

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers) + 1):
        sublists.append(numbers[i:j])

print(sublists)