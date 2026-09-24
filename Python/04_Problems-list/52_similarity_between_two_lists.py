list1 = ["red", "orange", "green", "blue", "white"]
list2 = ["black", "yellow", "green", "blue"]

list1_only = []
list2_only = []

for item in list1:
    if item not in list2:
        list1_only.append(item)

for item in list2:
    if item not in list1:
        list2_only.append(item)

print("Color1-Color2:", list1_only)
print("Color2-Color1:", list2_only)