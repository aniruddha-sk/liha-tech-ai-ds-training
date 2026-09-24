def add_three(x):
    return x + 3

def square(x):
    return x * x

def compose(first, second):
    def result(x):
        return second(first(x))
    return result

function = compose(add_three, square)

print(function(5))
