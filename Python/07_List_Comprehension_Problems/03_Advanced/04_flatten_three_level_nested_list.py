data = [[[1, 2], [3]], [[4, 5], [6]]]

res = []

for group in data:
    for row in group:
        for x in row:
            res.append(x)

print(res)