def my_filter(function, data):
    result = []

    for item in data:
        if function(item):
            result.append(item)

    return result

def is_even(x):
    return x % 2 == 0

print(my_filter(is_even, [1, 2, 3, 4, 5, 6]))
