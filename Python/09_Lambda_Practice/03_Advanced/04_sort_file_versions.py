versions = [
    ("app", "1.2.10"),
    ("app", "1.10.2"),
    ("app", "1.2.3")
]

def version_key(x):
    parts = x[1].split(".")
    return [int(i) for i in parts]

versions.sort(key=version_key)

print(versions)
