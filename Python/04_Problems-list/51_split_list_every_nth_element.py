letters = [
    "a", "b", "c", "d", "e", "f", "g",
    "h", "i", "j", "k", "l", "m", "n"
]

n = 3

for i in range(n):
    group = letters[i::n]
    print(group)