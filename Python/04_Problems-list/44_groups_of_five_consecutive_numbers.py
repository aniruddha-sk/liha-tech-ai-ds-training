numbers = list(range(1, 21))

for i in range(0, len(numbers), 5):
    group = numbers[i:i + 5]
    print(group)