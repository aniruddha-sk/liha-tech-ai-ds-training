def merge(intervals):
    intervals.sort()
    result = []

    for start, end in intervals:
        if not result or start > result[-1][1]:
            result.append([start, end])
        else:
            result[-1][1] = max(result[-1][1], end)

    return [tuple(x) for x in result]

intervals = [(1, 3), (2, 6), (8, 10), (9, 12)]
print(merge(intervals))
