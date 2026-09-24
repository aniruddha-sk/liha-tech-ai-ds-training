list1 = [1, 3, 5, 7, 9, 10]
list2 = [2, 4, 6, 8]

list1.pop()

for number in list2:
    list1.append(number)

print(list1)