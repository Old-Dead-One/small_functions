# Write a function add(x: float, y: float) -> float that adds two numbers.
# Write a function multiply(x: float, y: float) -> float that multiplies two numbers.
# Write a function square(x: float) -> float that squares a number (hint: it must use multiply).
# Write a function add_squares(x: float, y: float) -> float that adds the squares of two numbers (hint: it must use both add and square).

def add(x: float, y: float) -> float:
    return x + y

def multiply(x: float, y: float) -> float:
    return x * y

def square_x(x: float) -> float:
    return multiply(x, x)

def square_y(y: float) -> float:
    return multiply(y, y)

def add_squares(x: float, y: float) -> float:
    return add(square_x(x), square_y(y))

x = 3
y = 4

print("Add")
print(add(x, y))
print()
print("Multiply")
print(multiply(x, y))
print()
print("Square_x")
print(square_x(x))
print()
print("Square_y")
print(square_y(y))
print()
print("Add Squares")
print(add_squares(x, y))
