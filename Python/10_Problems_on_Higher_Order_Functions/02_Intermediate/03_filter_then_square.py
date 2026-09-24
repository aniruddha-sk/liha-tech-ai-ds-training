from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]

even = filter(lambda x: x % 2 == 0, numbers)
squares = map(lambda x: x * x, even)

print(list(squares))
