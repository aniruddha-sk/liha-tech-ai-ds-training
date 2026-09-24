def create_counter():
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count

    return counter

count = create_counter()

print(count())
print(count())
print(count())
print(count())
