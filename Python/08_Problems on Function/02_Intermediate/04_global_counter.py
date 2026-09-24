counter = 0

def count():
    global counter
    counter += 1
    return counter

print("Counter value =", count())
print("Counter value =", count())
print("Counter value =", count())
