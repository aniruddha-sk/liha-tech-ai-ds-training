points = [(3, 4), (1, 1), (-2, 2), (0, 5)]

points.sort(key=lambda x: abs(x[0]) + abs(x[1]))

print(points)
