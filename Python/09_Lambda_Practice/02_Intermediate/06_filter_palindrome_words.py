words = ["level", "python", "madam", "cloud", "radar"]

result = list(filter(lambda x: x == x[::-1], words))

print(result)
