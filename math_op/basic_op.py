def add(a, b) -> int:
    return a + b

def substract(a, b) -> int:
    return a - b

def multiply(a, b) -> int:
    return a * b

def divide( a, b) -> int:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b