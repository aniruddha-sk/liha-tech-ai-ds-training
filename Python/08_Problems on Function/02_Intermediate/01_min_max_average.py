def calculate(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    average = sum(numbers) / len(numbers)
    return minimum, maximum, average

a, b, c = calculate([12, 5, 30, 18, 9])

print("Minimum =", a)
print("Maximum =", b)
print("Average =", c)
