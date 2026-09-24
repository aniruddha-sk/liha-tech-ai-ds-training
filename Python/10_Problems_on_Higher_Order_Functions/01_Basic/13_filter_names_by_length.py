names = ["Asha", "Rohan", "Neha", "Sameer"]

def check_name(name):
    return len(name) >= 5

result = list(filter(check_name, names))

print(result)
