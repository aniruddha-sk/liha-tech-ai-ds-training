def common_prefix(words):
    prefix = words[0]

    for word in words[1:]:
        while not word.startswith(prefix):
            prefix = prefix[:-1]

    return prefix

words = ["flower", "flow", "flight"]
print("Longest common prefix =", common_prefix(words))
