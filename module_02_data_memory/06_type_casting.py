"""
Type Casting
────────────────────────────────────────────────────────────────────────────
Code examples and practice exercises from the lesson.
────────────────────────────────────────────────────────────────────────────
"""

# Example 1 — String to Integer
# Convert a string number to integer
num_str = "42"
num_int = int(num_str)

print(num_int)        # 42
print(type(num_int))  # <class 'int'>


# Example 2 — Integer to String
# Convert a number to string (for display or concatenation)
age = 25
age_str = str(age)

print(age_str)        # "25"
print(type(age_str))  # <class 'str'>


# Example 3 — String to Float
price = float("19.99")
print(price)          # 19.99
print(type(price))    # <class 'float'>


# Example 4 — Chained Conversions
# String → Int → Float
value = "42"
result = float(int(value))

print(result)         # 42.0
print(type(result))   # <class 'float'>


# Example 5 — Handling Conversion Errors
# Invalid conversion will crash your program without try/except
try:
    result = int("hello")
except ValueError:
    print("Cannot convert 'hello' to integer!")


# Example 6 — Base Conversions
# int() can convert from different number bases
binary = int("1010", 2)    # Binary to decimal
hex_num = int("FF", 16)    # Hexadecimal to decimal
octal = int("77", 8)       # Octal to decimal

print(f"Binary 1010 = {binary}")   # 10
print(f"Hex FF = {hex_num}")       # 255
print(f"Octal 77 = {octal}")       # 63


# Example 7 — Safe Conversion Function
def safe_int(value):
    """Convert to int safely, returning None on failure."""
    try:
        return int(value)
    except ValueError:
        return None

print(safe_int("42"))    # 42
print(safe_int("hello"))  # None


# ═══════════════════════════════════════════════════════════════════════════════
# PRACTICE EXERCISE
# ═══════════════════════════════════════════════════════════════════════════════
# 1. Convert string "100" to integer and multiply by 2
# 2. Convert integer 50 to string and concatenate with " dollars"
# 3. Try converting "hello" to integer and handle the error
# 4. Convert float 3.14159 to integer
# ═══════════════════════════════════════════════════════════════════════════════

# 1. Convert string "100" to integer and multiply by 2
value = int("100") * 2
print(f"100 * 2 = {value}")

# 2. Convert integer 50 to string and concatenate with " dollars"
price = str(50) + " dollars"
print(price)

# 3. Try converting "hello" to integer and handle the error
try:
    result = int("hello")
except ValueError:
    print("Cannot convert 'hello' to integer — ValueError!")

# 4. Convert float 3.14159 to integer
pi = int(3.14159)
print(f"int(3.14159) = {pi}")

# Try modifying it:
# - Convert a user input string to a number (simulated)
user_input = "25"
user_age = int(user_input)
print(f"Next year you'll be {user_age + 1}")