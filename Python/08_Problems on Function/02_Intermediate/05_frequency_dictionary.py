def frequency(items):
    result = {}
    for item in items:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result

print(frequency(["A", "B", "A", "C", "B", "A"]))
