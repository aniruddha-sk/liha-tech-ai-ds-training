for num in range(2, 49):
    count1 = 0
    count2 = 0

    for i in range(1, num + 1):
        if num % i == 0:
            count1 = count1 + 1

    next_num = num + 2

    for i in range(1, next_num + 1):
        if next_num % i == 0:
            count2 = count2 + 1

    if count1 == 2 and count2 == 2:
        print((num, next_num))