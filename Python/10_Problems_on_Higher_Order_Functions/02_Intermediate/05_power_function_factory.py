def create_power(exponent):
    def power(number):
        return number ** exponent
    return power

cube = create_power(3)

print(cube(4))
