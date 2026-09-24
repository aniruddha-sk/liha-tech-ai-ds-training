data = {"A": 1, "B": 2, "C": 1}

result = {}

for key, value in data.items():
    if value not in result:
        result[value] = []
    
    result[value].append(key)

print(result)