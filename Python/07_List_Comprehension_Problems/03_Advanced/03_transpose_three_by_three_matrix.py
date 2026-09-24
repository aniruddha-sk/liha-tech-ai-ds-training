matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

res = []

for col in range(3):
    row = []

    for i in range(3):
        row.append(matrix[i][col])

    res.append(row)

print(res)