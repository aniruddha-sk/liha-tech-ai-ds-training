numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [10, 11, 12],
    [7, 8, 9]
]

highest_list = numbers[0]
highest_sum = sum(numbers[0])

for item in numbers:
    current_sum = sum(item)

    if current_sum > highest_sum:
        highest_sum = current_sum
        highest_list = item

print(highest_list)