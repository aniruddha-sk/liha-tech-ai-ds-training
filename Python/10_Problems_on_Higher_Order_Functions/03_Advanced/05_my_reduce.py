def my_reduce(function, data):
    result = data[0]

    for item in data[1:]:
        result = function(result, item)

    return result

def add(a, b):
    return a + b

print(my_reduce(add, [10, 20, 30, 40]))
