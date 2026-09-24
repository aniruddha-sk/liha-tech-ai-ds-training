scores = {
    "Asha": 82,
    "Ravi": 74,
    "Neha": 91
}

result = max(scores, key=lambda x: scores[x])

print(result)
