def retry(function, retries):
    for attempt in range(1, retries + 1):
        try:
            return function(attempt)
        except:
            print("Failed on attempt", attempt)

    return "Failed"

def test(attempt):
    if attempt < 3:
        raise Exception()
    return "Success on attempt " + str(attempt)

print(retry(test, 3))
