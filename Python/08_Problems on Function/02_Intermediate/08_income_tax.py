def calculate_tax(income):
    if income <= 300000:
        return 0
    if income <= 600000:
        return (income - 300000) * 5 / 100

    tax = 300000 * 5 / 100
    tax += (income - 600000) * 10 / 100
    return tax

print("Tax =", calculate_tax(800000))
