data = {"A": 75, "B": 92, "C": 88}

max_key = max(data, key=data.get)

print("Key with maximum value =", max_key)