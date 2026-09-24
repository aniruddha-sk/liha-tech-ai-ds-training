data = {
    "student": {
        "name": "Amit",
        "marks": {
            "Python": 90
        }
    }
}

result = {}

result["student.name"] = data["student"]["name"]
result["student.marks.Python"] = data["student"]["marks"]["Python"]

print(result)