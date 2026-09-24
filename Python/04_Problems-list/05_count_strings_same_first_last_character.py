words = ["abc", "xyz", "aba", "1221"]

count = 0

for word in words:
    if len(word) >= 2:
        if word[0] == word[-1]:
            count = count + 1

print("Count =", count)