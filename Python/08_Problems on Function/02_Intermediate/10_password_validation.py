def validate_password(password):
    if len(password) < 8:
        return False, "Password must have at least 8 characters"

    upper = False
    digit = False

    for ch in password:
        if ch.isupper():
            upper = True
        if ch.isdigit():
            digit = True

    if not upper:
        return False, "Password needs an uppercase letter"
    if not digit:
        return False, "Password needs a digit"

    return True, "Password accepted"

status, reason = validate_password("Python123")
print("Valid =", status)
print("Reason =", reason)
