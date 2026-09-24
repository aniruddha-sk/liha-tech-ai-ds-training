data = {"fname": "Amit", "lname": "Patil"}

mapping = {
    "fname": "first_name",
    "lname": "last_name"
}

result = {}

for key, value in data.items():
    if key in mapping:
        result[mapping[key]] = value
    else:
        result[key] = value

print(result)