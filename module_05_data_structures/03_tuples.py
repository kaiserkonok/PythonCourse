"""
Tuples (The Immutable Lists)
────────────────────────────────────────────────────────────────────────────
Code examples and practice exercises from the lesson.
────────────────────────────────────────────────────────────────────────────
"""

# Example 1 — Creating Tuples
# Basic tuples
point = (3, 4)
colors = ("red", "green", "blue")
mixed = (1, "hello", 3.14)

print(point)    # (3, 4)
print(colors)   # ("red", "green", "blue")


# Example 2 — Accessing Items
record = ("Alice", 25, "Engineer")

print(record[0])  # Alice
print(record[-1]) # Engineer
print(record[1:]) # (25, "Engineer")


# Example 3 — Tuple Unpacking
# Unpack coordinates
point = (10, 20)
x, y = point
print(f"X: {x}, Y: {y}")

# Unpack record
name, age, job = ("Bob", 30, "Developer")
print(f"{name} is {age}, works as {job}")


# Example 4 — Swapping Values
a = 10
b = 20

# Pythonic way (tuple unpacking)
a, b = b, a
print(f"a: {a}, b: {b}")  # a: 20, b: 10


# Example 5 — Tuples as Dictionary Keys
# Tuples can be keys, lists cannot
locations = {
    (40, 74): "New York",
    (51, 0): "London",
    (35, 139): "Tokyo"
}

print(locations[(40, 74)])  # New York


# Example 6 — Returning Multiple Values
def get_name_age():
    return "Alice", 25  # Returns a tuple!

name, age = get_name_age()
print(f"{name} is {age}")  # Alice is 25


# ═══════════════════════════════════════════════════════════════════════════════
# PRACTICE EXERCISE
# ═══════════════════════════════════════════════════════════════════════════════
# 1. Create a tuple with your name, age, and city
# 2. Unpack the tuple into three variables
# 3. Try to modify the tuple and see the error
# 4. Use a tuple as a dictionary key
# ═══════════════════════════════════════════════════════════════════════════════

# 1. Create tuple
person = ("Charlie", 28, "London")

# 2. Unpack
name, age, city = person
print(f"{name}, {age}, lives in {city}")

# 3. Try to modify (will crash)
# person[0] = "David"  # TypeError: 'tuple' object does not support item assignment

# 4. Tuple as dict key
grades = {
    ("Alice", "Math"): 95,
    ("Bob", "Science"): 88
}
print(f"Alice Math: {grades[('Alice', 'Math')]}")

# Try modifying it:
# - Unpack with * (extended unpacking)
numbers = (1, 2, 3, 4, 5)
first, *middle, last = numbers
print(f"First: {first}, Middle: {middle}, Last: {last}")
