colors = ["Red", "Green", "White", "Black", "Pink", "Yellow"]

new_list = []

for i in range(len(colors)):
    if i != 0 and i != 4 and i != 5:
        new_list.append(colors[i])

print(new_list)