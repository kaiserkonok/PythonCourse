"""
Dynamic Typing
────────────────────────────────────────────────────────────────────────────
Code examples and practice exercises from the lesson.
────────────────────────────────────────────────────────────────────────────
"""

# Example 1 — Type Changes Automatically
value = 10
print(type(value))  # <class 'int'>

value = "hello"
print(type(value))  # <class 'str'>

value = 3.14
print(type(value))  # <class 'float'>


# Example 2 — Function Returns Different Types
def get_result(value):
    """Returns a string for large values, int for small."""
    if value > 10:
        return "Big"      # String
    else:
        return 0          # Integer

print(get_result(5))     # 0 (int)
print(get_result(15))    # Big (str)


# Example 3 — Type Hints (Optional)
def greet(name: str) -> str:
    """name: str means 'name should be a string'.
    -> str means 'this function returns a string'."""
    return f"Hello, {name}!"

print(greet("Alice"))


# Example 4 — Checking Types at Runtime
x = "hello"

# Using isinstance() — the Pythonic way
if isinstance(x, str):
    print(f"x is a string: {x.upper()}")

# You can check multiple types
y = 10
if isinstance(y, (int, float)):
    print(f"y is a number: {y}")


# Example 5 — When Dynamic Typing Bites You
def add_values(a, b):
    """Expects two numbers, but Python won't stop strings."""
    return a + b

# This works:
print(add_values(10, 5))      # 15 (int addition)
print(add_values(3.14, 2))    # 5.14 (float addition)

# But this also "works" — maybe not what you intended:
print(add_values("10", "5"))  # "105" (string concatenation!)


# Example 6 — Best Practices
# ✅ Use clear variable names that indicate type
user_name = "Alice"       # Clearly a string
user_count = 10           # Clearly an int
is_active = True          # Clearly a boolean

# ✅ Use type hints for functions
def calculate_total(price: float, quantity: int) -> float:
    return price * quantity

print(calculate_total(19.99, 3))


# ═══════════════════════════════════════════════════════════════════════════════
# PRACTICE EXERCISE
# ═══════════════════════════════════════════════════════════════════════════════
# 1. Create a variable with an integer
# 2. Print its type
# 3. Change it to a string
# 4. Print its type again
# 5. Use a type hint for a variable and see how it behaves
# ═══════════════════════════════════════════════════════════════════════════════

# 1. Create a variable with an integer
x = 42
print(f"x = {x}, type = {type(x)}")

# 2. Change it to a string
x = "hello"
print(f"x = {x}, type = {type(x)}")

# 3. Use a type hint for a variable
name: str = "Alice"
age: int = 25
print(f"{name} is {age} years old")
print(f"name type: {type(name)}")
print(f"age type: {type(age)}")