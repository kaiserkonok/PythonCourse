"""
Computer Architecture for Coders
────────────────────────────────────────────────────────────────────────────
Code examples and practice exercises from the lesson.
────────────────────────────────────────────────────────────────────────────
"""

# Example 1 — Simple Variable Assignment
# Python decides where in RAM to store 10
# You don't need to know the exact memory address
x = 10
print(x)  # Output: 10


# Example 2 — Multiple Variables
# Each variable gets its own space in RAM
name = "Python"
version = 3.12
is_awesome = True

print(f"{name} {version} is awesome: {is_awesome}")


# Example 3 — Math Operations (CPU Does the Work)
a = 100
b = 50
result = a + b
print(result)  # Output: 150


# Example 4 — Variable Reassignment
# Variables can be reassigned
# Python updates the value at that memory location
count = 1
print(count)  # 1
count = 2     # Old value is replaced
print(count)  # 2


# Example 5 — Type Information is Stored Too
# Python stores both the value AND the type in RAM
x = 42        # int
y = 3.14      # float
z = "hello"   # str

print(type(x))  # <class 'int'>
print(type(y))  # <class 'float'>
print(type(z))  # <class 'str'>


# ═══════════════════════════════════════════════════════════════════════════════
# PRACTICE EXERCISE
# ═══════════════════════════════════════════════════════════════════════════════
# Run this code and observe the output:
#   x = 5
#   y = 10
#   z = x + y
#   print(f"x = {x}, y = {y}, z = {z}")
#
# Think about: Where do x, y, and z live in RAM?
#              What does the CPU do with these values?
# ═══════════════════════════════════════════════════════════════════════════════

x = 5
y = 10
z = x + y
print(f"x = {x}, y = {y}, z = {z}")

# Answer: x, y, and z each get their own address in RAM.
# The CPU fetches x and y from RAM, adds them, then stores
# the result (15) in z's location in RAM.