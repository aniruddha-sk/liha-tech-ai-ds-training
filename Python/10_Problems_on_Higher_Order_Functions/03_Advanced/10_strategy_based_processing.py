def normalize(data):
    minimum = min(data)
    maximum = max(data)

    return [(x - minimum) / (maximum - minimum) for x in data]

def process(data, mode):
    if mode == "normalize":
        return normalize(data)

    return data

print(process([10, 20, 30], "normalize"))
