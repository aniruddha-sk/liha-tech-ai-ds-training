def repeat_function(function, times):
    result = []

    for i in range(times):
        result.append(function())

    return result

def hello():
    return "Hello"

print(repeat_function(hello, 3))
