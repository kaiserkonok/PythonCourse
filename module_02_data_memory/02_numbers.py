"""
Numbers (Int, Float, Complex)
────────────────────────────────────────────────────────────────────────────
Code examples and practice exercises from the lesson.
────────────────────────────────────────────────────────────────────────────
"""

# Example 1 — Integer Operations
# All basic math with integers
a = 10
b = 3

print(a + b)     # 13 (addition)
print(a - b)     # 7  (subtraction)
print(a * b)     # 30 (multiplication)
print(a / b)     # 3.333... (division → always float!)
print(a // b)    # 3  (floor division → rounds down)
print(a % b)     # 1  (modulus → remainder)
print(a ** b)    # 1000 (exponent → 10^3)


# Example 2 — Float Operations
# Floats work the same way
x = 10.5
y = 2.0

print(x + y)     # 12.5
print(x * y)     # 21.0
print(x / y)     # 5.25


# Example 3 — Mixed int and float
# When int and float mix, the result is always float
i = 10     # int
f = 2.5    # float

print(i + f)    # 12.5 (float)
print(i * f)    # 25.0 (float)


# Example 4 — Complex Numbers
# Complex numbers have real and imaginary parts
c1 = 3 + 4j
c2 = 1 + 2j

print(c1 + c2)     # (4+6j)
print(c1 * c2)     # (-5+10j)

# Access parts
c = 3 + 4j
print(c.real)      # 3.0
print(c.imag)      # 4.0


# Example 5 — Checking Types
# Every number has a type
x = 42
y = 3.14
z = 3 + 4j

print(type(x))     # <class 'int'>
print(type(y))     # <class 'float'>
print(type(z))     # <class 'complex'>


# Example 6 — The Floating-Point Gotcha
# This surprises everyone!
print(0.1 + 0.2)   # 0.30000000000000004 (not 0.3!)

# Solution for money: use integers (cents)
price_cents = 10 + 20
print(f"Price: ${price_cents / 100:.2f}")  # $0.30


# ═══════════════════════════════════════════════════════════════════════════════
# PRACTICE EXERCISE
# ═══════════════════════════════════════════════════════════════════════════════
# 1. Create an integer variable for your age
# 2. Create a float variable for your height in meters
# 3. Calculate your age in 10 years
# 4. Print both using an f-string
#
# Bonus: Create a complex number and print its real and imaginary parts.
# ═══════════════════════════════════════════════════════════════════════════════

my_age = 25
my_height = 1.75
age_in_10_years = my_age + 10

print(f"Current age: {my_age}")
print(f"Height: {my_height}m")
print(f"In 10 years, I will be {age_in_10_years} years old")

# Bonus:
complex_num = 5 + 3j
print(f"Complex: {complex_num}")
print(f"Real part: {complex_num.real}")
print(f"Imaginary part: {complex_num.imag}")