text = "mississippi"

frequency = {}

for char in text:
    if char in frequency:
        frequency[char] = frequency[char] + 1
    else:
        frequency[char] = 1

result = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

print(result)