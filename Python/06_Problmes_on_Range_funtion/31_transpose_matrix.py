matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

rows = len(matrix)
columns = len(matrix[0])

transpose = []

for j in range(columns):
    row = []

    for i in range(rows):
        row.append(matrix[i][j])

    transpose.append(row)

print(transpose)