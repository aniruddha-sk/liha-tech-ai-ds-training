numbers = [4, 2, 4, 3, 2, 5, 4, 3]

res = []

for x in numbers:
    if numbers.count(x) > 1 and x not in res:
        res.append(x)

print(res)