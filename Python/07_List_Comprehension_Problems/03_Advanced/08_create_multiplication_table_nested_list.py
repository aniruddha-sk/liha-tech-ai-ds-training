res = []

for i in range(1, 6):

    row = []

    for j in range(1, 6):
        row.append(i * j)

    res.append(row)

print(res)