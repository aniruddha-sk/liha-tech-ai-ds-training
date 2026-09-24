def count_vowels(text):
    count = 0
    for ch in text:
        if ch.lower() in "aeiou":
            count += 1
    return count

print("Vowel count =", count_vowels("Programming"))
