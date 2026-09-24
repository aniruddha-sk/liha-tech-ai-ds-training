from functools import reduce

numbers = [1, 2, 3, 4]

squares = map(lambda x: x * x, numbers)
result = reduce(lambda a, b: a + b, squares)

print("Sum of squares =", result)
