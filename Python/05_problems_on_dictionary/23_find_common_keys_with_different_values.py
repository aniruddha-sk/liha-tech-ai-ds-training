D1 = {"a": 1, "b": 2, "c": 3}
D2 = {"b": 20, "c": 3, "d": 4}

result = {}

for key in D1:
    if key in D2:
        if D1[key] != D2[key]:
            result[key] = D1[key]

print(result)