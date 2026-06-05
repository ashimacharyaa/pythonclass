try:
    x = 1 / 0
except ZeroDivisionError:
    print("Logging error")
    raise  # sends error again upward