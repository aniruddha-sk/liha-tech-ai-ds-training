sentence = "python is easy and python is powerful"

words = sentence.split()

result = {}

for i in range(len(words)):
    word = words[i]

    if word not in result:
        result[word] = []

    result[word].append(i)

print(result)