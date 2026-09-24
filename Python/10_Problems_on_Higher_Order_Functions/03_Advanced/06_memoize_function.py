def memoize(function):
    cache = {}

    def wrapper(value):
        if value not in cache:
            cache[value] = function(value)
        return cache[value]

    return wrapper

count = 0

def square(x):
    global count
    count += 1
    return x * x

square = memoize(square)

print(square(5))
print(square(5))
print(square(7))
print("Actual calculations =", count)
