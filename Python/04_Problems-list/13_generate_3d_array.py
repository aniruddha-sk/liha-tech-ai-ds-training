array = []

for i in range(3):
    layer = []

    for j in range(4):
        row = []

        for k in range(6):
            row.append("*")

        layer.append(row)

    array.append(layer)

print(array)