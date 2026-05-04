"""
Arithmetic Operators (Math in Python)
────────────────────────────────────────────────────────────────────────────
Code examples and practice exercises from the lesson.
────────────────────────────────────────────────────────────────────────────
"""

# Example 1 — Basic Arithmetic
a = 10
b = 3

print(f"{a} + {b} = {a + b}")   # 13
print(f"{a} - {b} = {a - b}")   # 7
print(f"{a} * {b} = {a * b}")   # 30
print(f"{a} / {b} = {a / b}")   # 3.333...


# Example 2 — Floor Division vs True Division
# True division — always returns float
print(10 / 3)    # 3.3333333333333335
print(10 / 2)    # 5.0 (still a float!)

# Floor division — rounds down, returns int
print(10 // 3)   # 3
print(10 // 2)   # 5


# Example 3 — Modulus in Action
# Check if a number is even
x = 10
print(f"{x} is even: {x % 2 == 0}")  # True

# Check divisibility
y = 25
print(f"{y} divisible by 5: {y % 5 == 0}")  # True

# Wrap around (like a clock)
hour = 23
next_hour = (hour + 1) % 24
print(f"Next hour: {next_hour}")  # 0 (midnight)


# Example 4 — Exponentiation
# Power
print(2 ** 10)     # 1024 (2^10)
print(5 ** 3)      # 125 (5^3)

# Square root (using 0.5)
print(16 ** 0.5)   # 4.0
print(27 ** (1/3)) # 3.0 (cube root)


# Example 5 — Order of Operations (PEMDAS)
# Python follows PEMDAS:
# Parentheses → Exponents → Multiplication/Division → Addition/Subtraction

result = 2 + 3 * 4       # 14 (multiply first)
result = (2 + 3) * 4     # 20 (parentheses first)
result = 2 ** 3 * 4      # 32 (exponent first, then multiply)
result = 2 ** (3 * 4)    # 16777216 (parentheses first)

print(f"2 ** (3 * 4) = {result}")


# Example 6 — Augmented Assignment
score = 100

# Instead of: score = score + 10
score += 10
print(f"Score: {score}")  # 110

# Instead of: score = score - 5
score -= 5
print(f"Score: {score}")  # 105

# Instead of: score = score * 2
score *= 2
print(f"Score: {score}")  # 210


# ═══════════════════════════════════════════════════════════════════════════════
# PRACTICE EXERCISE
# ═══════════════════════════════════════════════════════════════════════════════
# 1. Calculate the area of a rectangle (length = 12, width = 5)
# 2. Find the remainder when 47 is divided by 7
# 3. Use exponentiation to calculate 2^8
# 4. Use augmented assignment to increment a counter from 0 to 10
# ═══════════════════════════════════════════════════════════════════════════════

# 1. Area of rectangle
length = 12
width = 5
area = length * width
print(f"Area: {area}")

# 2. Remainder
remainder = 47 % 7
print(f"47 % 7 = {remainder}")

# 3. Exponentiation
result = 2 ** 8
print(f"2^8 = {result}")

# 4. Augmented assignment
counter = 0
counter += 10
print(f"Counter: {counter}")

# Try modifying it:
# - Calculate the area of a circle with radius 7 (use 3.14159 for pi)
radius = 7
pi = 3.14159
circle_area = pi * radius ** 2
print(f"Circle area: {circle_area}")
