words = ["apple", "banana", "avocado", "ball", "cat", "car"]

groups = {}

for word in words:
    first = word[0]

    if first not in groups:
        groups[first] = []

    groups[first].append(word)

print(groups)