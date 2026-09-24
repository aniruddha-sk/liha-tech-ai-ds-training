numbers = [1, 2, 3, 4, 5, 6, 7, 8]

odd_numbers = []

for number in numbers:
    if number % 2 != 0:
        odd_numbers.append(number)

print(odd_numbers)