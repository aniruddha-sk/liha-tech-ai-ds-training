inventory = {
    "Pen": 10,
    "Book": 5
}

transactions = [
    ("Pen", -3),
    ("Book", 4),
    ("Pencil", 6)
]

for item, quantity in transactions:
    if item in inventory:
        inventory[item] = inventory[item] + quantity
    else:
        inventory[item] = quantity

print(inventory)