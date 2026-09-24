calculator = {
    "add": lambda a, b: a + b,
    "subtract": lambda a, b: a - b,
    "multiply": lambda a, b: a * b,
    "divide": lambda a, b: a / b
}

operation = "multiply"
a = 7
b = 6

print("Result =", calculator[operation](a, b))
