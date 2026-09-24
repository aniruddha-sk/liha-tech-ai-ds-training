transactions = [
    ("T3", 500),
    ("T1", 700),
    ("T2", 700),
    ("T4", 300)
]

transactions.sort(key=lambda x: (-x[1], x[0]))

print(transactions)
