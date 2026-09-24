list1 = [1, 2, 3, 4]
list2 = [5, 6, 3, 8]

common = False

for item in list1:
    if item in list2:
        common = True

print(common)