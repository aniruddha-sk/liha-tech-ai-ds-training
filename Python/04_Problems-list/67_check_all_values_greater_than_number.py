numbers = [10, 20, 30, 40, 50]

given_number = 5

all_greater = True

for number in numbers:
    if number <= given_number:
        all_greater = False

print(all_greater)