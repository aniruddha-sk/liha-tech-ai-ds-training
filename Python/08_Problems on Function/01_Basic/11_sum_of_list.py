def list_sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

print("Sum =", list_sum([10, 20, 30, 40]))
