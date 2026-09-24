D1 = {"a": 10, "b": 20}
D2 = {"b": 5, "c": 15}

result = D1.copy()

for key, value in D2.items():
    if key in result:
        result[key] = result[key] + value
    else:
        result[key] = value

print(result)