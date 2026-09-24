res = [
    x for x in range(2, 31)
    if all(x % i != 0 for i in range(2, int(x ** 0.5) + 1))
]

print(res)