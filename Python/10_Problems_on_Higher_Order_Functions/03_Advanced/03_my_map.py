def my_map(function, data):
    result = []

    for item in data:
        result.append(function(item))

    return result

def square(x):
    return x * x

print(my_map(square, [1, 2, 3, 4]))
