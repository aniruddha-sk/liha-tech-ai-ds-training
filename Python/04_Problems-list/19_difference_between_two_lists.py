list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

difference = []

for item in list1:
    if item not in list2:
        difference.append(item)

print(difference)