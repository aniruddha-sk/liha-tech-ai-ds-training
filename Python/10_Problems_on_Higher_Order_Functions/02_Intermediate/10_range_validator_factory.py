def create_validator(minimum, maximum):
    def validate(value):
        return minimum <= value <= maximum
    return validate

validator = create_validator(18, 60)

print("Valid =", validator(25))
