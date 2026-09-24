numbers = [1, 2, 3, 4, 5]

sublist = [2, 3]

if sublist in [numbers[i:i + len(sublist)] for i in range(len(numbers))]:
    print("Sublist exists")
else:
    print("Sublist does not exist")