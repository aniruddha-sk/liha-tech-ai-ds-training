data = {
    "name": "Amit",
    "address": {
        "city": "Pune",
        "details": {
            "area": "Hadapsar"
        }
    }
}

def find_depth(dictionary):
    depth = 1

    for value in dictionary.values():
        if isinstance(value, dict):
            current_depth = 1 + find_depth(value)

            if current_depth > depth:
                depth = current_depth

    return depth


print("Depth =", find_depth(data))