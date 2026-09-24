from functools import reduce

numbers = [12, 45, 7, 91, 33]

result = reduce(lambda a, b: a if a > b else b, numbers)

print("Largest =", result)
