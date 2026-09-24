D1 = {
    "a": 1,
    "b": {
        "x": 10
    }
}

D2 = {
    "b": {
        "y": 20
    },
    "c": 3
}

result = D1.copy()

for key, value in D2.items():

    if key in result and isinstance(result[key], dict) and isinstance(value, dict):
        result[key].update(value)
    else:
        result[key] = value

print(result)