numbers = [[1, 2], [3, 4], [5, 6]]

new_list = []

for item in numbers:
    for number in item:
        new_list.append(number)

print(new_list)