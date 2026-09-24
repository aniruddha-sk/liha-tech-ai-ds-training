def add(a):
    def second(b):
        def third(c):
            return a + b + c
        return third
    return second

print(add(10)(20)(30))
