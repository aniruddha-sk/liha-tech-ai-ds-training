numbers = [5, 10, 15, 20, 25, 30, 35]

start = 10
end = 25

count = 0

for number in numbers:
    if number >= start and number <= end:
        count = count + 1

print("Count =", count)