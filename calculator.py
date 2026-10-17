CONTRIBUTORS = [ seemal]
CONTRIBUTORS = [Araib,Prathmesh]

def add(a, b):
    return a + b

def subtract(a, b):
    return a-b
    
def multiply(a, b):
    return a*b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

if __name__ == "__main__":
    print(f"Welcome to the Group Calculator!, written by {seemal}")
    print(add(2, 2))
    print(subtract(5, 2))
    print(f"Welcome to the Group Calculator!, written by {Araib}")
    print(f"Welcome to the Group Calculator!, written by {Prathmesh}")
    print(add(2, 2))
    print(divide(7,2))
    print(multiply(2,3))
