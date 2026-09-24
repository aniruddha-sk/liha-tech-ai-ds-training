list1 = ["a", "b", "c", "d", "e"]
list2 = ["d", "e", "f", "g", "h"]

missing = []
additional = []

for item in list1:
    if item not in list2:
        missing.append(item)

for item in list2:
    if item not in list1:
        additional.append(item)

print("Missing values:", missing)
print("Additional values:", additional)