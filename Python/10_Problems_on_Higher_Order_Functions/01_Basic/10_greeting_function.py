def create_greeting(language):
    if language == "Marathi":
        return lambda name: "Namaskar, " + name + "!"
    else:
        return lambda name: "Hello, " + name + "!"

greet = create_greeting("Marathi")

print(greet("Asha"))
