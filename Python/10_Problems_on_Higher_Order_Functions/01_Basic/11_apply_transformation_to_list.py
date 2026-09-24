def cube(x):
    return x * x * x

def transform(data, function):
    result = []

    for item in data:
        result.append(function(item))

    return result

print(transform([1, 2, 3], cube))
