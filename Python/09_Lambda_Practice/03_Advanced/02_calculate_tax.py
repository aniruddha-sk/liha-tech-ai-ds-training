income = 800000

tax = lambda x: 0 if x <= 300000 else (x - 300000) * 0.05 if x <= 600000 else 15000 + (x - 600000) * 0.10

print("Tax =", tax(income))
