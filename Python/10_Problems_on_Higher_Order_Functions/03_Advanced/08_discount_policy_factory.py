def create_discount(policy):
    if policy == "premium":
        return lambda price: price * 0.85
    elif policy == "regular":
        return lambda price: price * 0.90
    return lambda price: price

discount = create_discount("premium")

print("Final price =", discount(2000))
