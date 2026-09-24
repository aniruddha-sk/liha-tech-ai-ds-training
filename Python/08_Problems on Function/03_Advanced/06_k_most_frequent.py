def most_frequent(numbers, k):
    frequency = {}

    for number in numbers:
        frequency[number] = frequency.get(number, 0) + 1

    numbers = sorted(frequency, key=frequency.get, reverse=True)
    return numbers[:k]

numbers = [1, 1, 1, 2, 2, 3]
print(most_frequent(numbers, 2))
