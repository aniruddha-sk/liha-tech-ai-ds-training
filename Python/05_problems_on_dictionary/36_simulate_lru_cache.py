capacity = 3

requests = ["A", "B", "C", "A", "D"]

cache = {}

for item in requests:

    if item in cache:
        del cache[item]

    cache[item] = True

    if len(cache) > capacity:
        oldest = next(iter(cache))
        del cache[oldest]

print("Final cache order (oldest to newest) =", list(cache.keys()))