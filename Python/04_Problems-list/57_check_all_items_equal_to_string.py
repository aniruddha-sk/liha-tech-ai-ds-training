words = ["apple", "apple", "apple"]

given_word = "apple"

all_same = True

for word in words:
    if word != given_word:
        all_same = False

print(all_same)