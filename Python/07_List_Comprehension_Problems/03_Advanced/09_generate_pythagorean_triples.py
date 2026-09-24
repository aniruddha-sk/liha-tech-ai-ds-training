res = []

for a in range(1, 21):

    for b in range(a + 1, 21):

        for c in range(b + 1, 21):

            if a * a + b * b == c * c:
                res.append((a, b, c))

print(res)