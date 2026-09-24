def square(x):
    return x * x

def cube(x):
    return x * x * x

def double(x):
    return x * 2

def apply_functions(functions, value):
    result = []

    for function in functions:
        result.append(function(value))

    return result

functions = [square, cube, double]

print(apply_functions(functions, 3))
