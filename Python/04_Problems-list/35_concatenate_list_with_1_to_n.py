letters = ["p", "q"]
n = 5

new_list = []

for i in range(1, n + 1):
    for letter in letters:
        new_list.append(letter + str(i))

print(new_list)