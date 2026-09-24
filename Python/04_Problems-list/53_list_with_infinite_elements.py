def numbers():
    i = 1

    while True:
        yield i
        i = i + 1


for number in numbers():
    print(number)

    if number == 10:
        break