matrix = [[1, 2, 3], [4, 5, 6], [7, 8]]

res = [x for row in matrix for x in row if x % 2 == 0]

print(res)