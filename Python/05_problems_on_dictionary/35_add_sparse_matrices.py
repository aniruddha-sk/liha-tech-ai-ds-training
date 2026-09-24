A = {
    (0, 0): 2,
    (1, 1): 3
}

B = {
    (0, 0): 5,
    (0, 1): 4
}

result = A.copy()

for position, value in B.items():

    if position in result:
        result[position] = result[position] + value
    else:
        result[position] = value

print(result)