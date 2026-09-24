import itertools

numbers = [1, 2, 3]

permutations = itertools.permutations(numbers)

for item in permutations:
    print(item)