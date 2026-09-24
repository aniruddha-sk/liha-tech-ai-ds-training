def create_multiplier(number):
    def multiply(value):
        return value * number

    return multiply

multiply_by_5 = create_multiplier(5)

print(multiply_by_5(8))
