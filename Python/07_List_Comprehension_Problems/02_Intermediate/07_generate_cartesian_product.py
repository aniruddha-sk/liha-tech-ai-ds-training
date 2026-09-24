list1 = [1, 2]
list2 = ['A', 'B']

res = [(x, y) for x in list1 for y in list2]

print(res)