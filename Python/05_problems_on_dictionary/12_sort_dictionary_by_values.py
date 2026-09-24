data = {"a": 30, "b": 10, "c": 20}

sorted_data = dict(sorted(data.items(), key=lambda item: item[1]))

print(sorted_data)