data = {"a": 10, "b": 20, "c": 30}

result = {}

for key, value in data.items():
    result[value] = key

print(result)