CONTRIBUTORS = []

def add(a, b):
    pass

def subtract(a, b):
    pass

def multiply(a, b):
    return a*b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

if __name__ == "__main__":
    print(f"Welcome to the Group Calculator!, written by {CONTRIBUTORS}")
    print(add(2, 2))
    print(divide(7,2))
    print(multiply(2,3))