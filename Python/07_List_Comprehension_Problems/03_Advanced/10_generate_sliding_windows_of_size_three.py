numbers = [10, 20, 30, 40, 50, 60]

res = []

for i in range(len(numbers) - 2):

    window = numbers[i:i + 3]

    res.append(window)

print(res)