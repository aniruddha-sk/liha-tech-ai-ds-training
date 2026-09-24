matrix = [
    [2, 4, 6],
    [1, 3, 5],
    [10, 20, 30]
]

res = []

for row in matrix:
    res.append(sum(row))

print(res)