def aggregate(data, function):
    result = data[0]

    for item in data[1:]:
        result = function(result, item)

    return result

def maximum(a, b):
    if a > b:
        return a
    return b

print(aggregate([10, 20, 30, 40], maximum))
