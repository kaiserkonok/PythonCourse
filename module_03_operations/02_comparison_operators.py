"""
Comparison Operators (Asking Questions)
────────────────────────────────────────────────────────────────────────────
Code examples and practice exercises from the lesson.
────────────────────────────────────────────────────────────────────────────
"""

# Example 1 — Basic Comparisons
a = 10
b = 5

print(f"{a} > {b}: {a > b}")    # True
print(f"{a} < {b}: {a < b}")    # False
print(f"{a} == {b}: {a == b}")  # False
print(f"{a} != {b}: {a != b}")  # True


# Example 2 — Comparison with Variables
age = 20
minimum_age = 18

can_vote = age >= minimum_age
print(f"Can vote: {can_vote}")  # True

score = 95
passing_score = 50

passed = score >= passing_score
print(f"Passed: {passed}")  # True


# Example 3 — String Comparisons
name1 = "Alice"
name2 = "Bob"

print(f"{name1} < {name2}: {name1 < name2}")  # True (alphabetical)
print(f"{name1} == {name2}: {name1 == name2}")  # False

# Case sensitivity matters
print(f"'python' == 'Python': {'python' == 'Python'}")  # False

# Case-insensitive comparison
print(f"'python'.lower() == 'Python'.lower(): {'python'.lower() == 'Python'.lower()}")  # True


# Example 4 — Chained Comparisons
x = 15

# Traditional way
print(x > 10 and x < 20)   # True

# Pythonic chained way
print(10 < x < 20)         # True

# Check if in range
print(0 <= x <= 100)       # True (percentage check)


# Example 5 — Comparing Different Types
# Numbers vs Strings — never equal
print(5 == "5")     # False
print(5 != "5")     # True

# Booleans are special — True is 1, False is 0
print(True == 1)    # True
print(False == 0)   # True
print(True > 0)     # True


# Example 6 — The `is` vs `==` Gotcha
# == checks if values are equal
# is checks if they are the exact same object in memory

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)   # True (same values)
print(a is b)   # False (different objects!)

# For simple values, Python optimizes and they may be the same
x = 10
y = 10
print(x == y)   # True
print(x is y)   # True (small integers are cached)


# ═══════════════════════════════════════════════════════════════════════════════
# PRACTICE EXERCISE
# ═══════════════════════════════════════════════════════════════════════════════
# 1. Compare two numbers: 25 and 18 — is the first greater?
# 2. Check if your name equals "Alice"
# 3. Use a chained comparison to check if a number is between 1 and 100
# 4. Compare two strings case-insensitively
# ═══════════════════════════════════════════════════════════════════════════════

# 1. Compare numbers
print(f"25 > 18: {25 > 18}")

# 2. Check name
my_name = "Alice"
print(f"Name is Alice: {my_name == 'Alice'}")

# 3. Chained comparison
num = 50
print(f"1 <= {num} <= 100: {1 <= num <= 100}")

# 4. Case-insensitive comparison
str1 = "Python"
str2 = "python"
print(f"Case-insensitive equal: {str1.lower() == str2.lower()}")

# Try modifying it:
# - Compare the length of two strings
name_a = "Alice"
name_b = "Bob"
print(f"Length of '{name_a}' < length of '{name_b}': {len(name_a) < len(name_b)}")
