def gross_salary(basic, hra_percent, da_percent):
    def amount(percent):
        return basic * percent / 100

    hra = amount(hra_percent)
    da = amount(da_percent)
    return basic + hra + da

print("Gross salary =", gross_salary(30000, 20, 10))
