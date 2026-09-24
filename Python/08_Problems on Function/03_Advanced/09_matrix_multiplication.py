def multiply(A, B):
    result = []

    for i in range(len(A)):
        row = []

        for j in range(len(B[0])):
            total = 0

            for k in range(len(B)):
                total += A[i][k] * B[k][j]

            row.append(total)

        result.append(row)

    return result

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

print(multiply(A, B))
