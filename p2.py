def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero is not allowed."
    else:
        return x / y

# Test addition
assert add(3, 5) == 8
assert add(-3, 5) == 2
assert add(0, 0) == 0

# Test subtraction
assert subtract(5, 3) == 2
assert subtract(-3, 5) == -8
assert subtract(0, 0) == 0

# Test multiplication
assert multiply(3, 5) == 15
assert multiply(-3, 5) == -15
assert multiply(0, 5) == 0

# Test division
assert divide(10, 2) == 5
assert divide(-10, 2) == -5
assert divide(5, 0) == "Error! Division by zero is not allowed."
assert divide(0, 5) == 0

print("All tests passed successfully!")
