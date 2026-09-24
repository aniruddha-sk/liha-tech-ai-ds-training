scores = {
    "A": 95,
    "B": 82,
    "C": 95,
    "D": 70
}

sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)

rank = 0
previous_score = None

for player, score in sorted_scores:

    if score != previous_score:
        rank = rank + 1

    print("Rank", rank, ":", player, "(", score, ")")

    previous_score = score