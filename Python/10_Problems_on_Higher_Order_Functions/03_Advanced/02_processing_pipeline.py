def double(x):
    return x * 2

def add_one(x):
    return x + 1

def square(x):
    return x * x

def pipeline(functions, value):
    for function in functions:
        value = function(value)
    return value

functions = [double, add_one, square]

print(pipeline(functions, 3))
