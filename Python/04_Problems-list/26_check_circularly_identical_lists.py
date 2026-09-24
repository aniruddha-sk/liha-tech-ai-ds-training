list1 = [1, 2, 3, 4]
list2 = [3, 4, 1, 2]

combined = list1 + list1

if len(list1) == len(list2) and list2 == combined[:len(list2)]:
    print("Circularly identical")
else:
    print("Not circularly identical")