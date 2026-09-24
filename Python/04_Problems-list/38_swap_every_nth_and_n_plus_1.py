numbers = [0, 1, 2, 3, 4, 5]

for i in range(0, len(numbers), 2):
    numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]

print(numbers)