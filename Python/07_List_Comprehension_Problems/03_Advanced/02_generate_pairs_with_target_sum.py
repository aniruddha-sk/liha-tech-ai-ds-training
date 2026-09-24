numbers = [1, 2, 3, 4, 5, 6]
target = 7

res = []

for x in numbers:
    for y in numbers:
        if x < y and x + y == target:
            res.append((x, y))

print(res)