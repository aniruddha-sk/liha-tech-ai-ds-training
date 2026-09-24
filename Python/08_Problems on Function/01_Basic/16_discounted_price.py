def final_price(price, discount):
    amount = price * discount / 100
    return price - amount

print("Final price =", final_price(2500, 10))
