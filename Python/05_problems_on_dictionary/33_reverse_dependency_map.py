tasks = {
    "Deploy": ["Test"],
    "Test": ["Build"],
    "Build": ["Code"]
}

result = {}

for task, prerequisites in tasks.items():

    for prerequisite in prerequisites:

        if prerequisite not in result:
            result[prerequisite] = []

        result[prerequisite].append(task)

print(result)