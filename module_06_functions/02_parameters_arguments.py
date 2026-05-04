"""
Parameters & Arguments (Flexible Function Inputs)
────────────────────────────────────────────────────────────────────────────
Code examples and practice exercises from the lesson.
────────────────────────────────────────────────────────────────────────────
"""

# Example 1 — Positional Arguments
def describe(name, age, city):
    print(f"{name} is {age}, lives in {city}")

describe("Alice", 25, "NY")  # Order matters!


# Example 2 — Keyword Arguments
describe(age=25, city="NY", name="Alice")  # Order doesn't matter!


# Example 3 — Default Values
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")           # Hello, Alice!
greet("Bob", "Hi")       # Hi, Bob!


# Example 4 — *args (Variable Positional)
def total(*numbers):
    return sum(numbers)

print(total(1, 2, 3))      # 6
print(total(10, 20, 30, 40))  # 100


# Example 5 — **kwargs (Variable Keyword)
def build_profile(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

build_profile(name="Alice", age=25, job="Dev")


# Example 6 — Combining All
def full_example(a, b, *args, x=10, y=20, **kwargs):
    print(f"Positional: {a}, {b}")
    print(f"Extra: {args}")
    print(f"Keywords: {x}, {y}")
    print(f"Extra kwargs: {kwargs}")

full_example(1, 2, 3, 4, 5, x=100, y=200, z=300)


# ═══════════════════════════════════════════════════════════════════════════════
# PRACTICE EXERCISE
# ═══════════════════════════════════════════════════════════════════════════════
# 1. Create a function with default parameters
# 2. Write a function that takes *args and returns their product
# 3. Use **kwargs to create a flexible config function
# 4. Combine positional, *args, and **kwargs
# ═══════════════════════════════════════════════════════════════════════════════

# 1. Function with defaults
def create_user(name, role="guest", active=True):
    return {"name": name, "role": role, "active": active}

print(create_user("Alice"))
print(create_user("Bob", "admin", False))

# 2. Product of *args
def product(*nums):
    result = 1
    for n in nums:
        result *= n
    return result

print(f"Product: {product(2, 3, 4)}")

# 3. Flexible config
def setup_config(**settings):
    defaults = {"theme": "dark", "font": "12px"}
    defaults.update(settings)
    return defaults

config = setup_config(theme="light", lang="en")
print(f"Config: {config}")

# 4. Combine all
def order(item, *sides, drink="water", **extras):
    print(f"Main: {item}")
    print(f"Sides: {sides}")
    print(f"Drink: {drink}")
    print(f"Extras: {extras}")

order("Burger", "Fries", "Salad", drink="Coke", tip=5)

# Try modifying it:
# - Use * to unpack a list into arguments
def add_three(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
print(f"Unpacked sum: {add_three(*numbers)}")
