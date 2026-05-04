"""
Logical Operators (Combining Conditions)
────────────────────────────────────────────────────────────────────────────
Code examples and practice exercises from the lesson.
────────────────────────────────────────────────────────────────────────────
"""

# Example 1 — Basic `and`
is_adult = True
has_license = True

# Both must be True
can_drive = is_adult and has_license
print(f"Can drive: {can_drive}")  # True

# One is False
has_license = False
can_drive = is_adult and has_license
print(f"Can drive: {can_drive}")  # False


# Example 2 — Basic `or`
is_weekend = False
is_holiday = True

# At least one must be True
can_sleep_in = is_weekend or is_holiday
print(f"Can sleep in: {can_sleep_in}")  # True

# Both False
is_holiday = False
can_sleep_in = is_weekend or is_holiday
print(f"Can sleep in: {can_sleep_in}")  # False


# Example 3 — Basic `not`
is_raining = True

# Invert the value
print(f"It is raining: {is_raining}")        # True
print(f"It is NOT raining: {not is_raining}") # False


# Example 4 — Combining Multiple Operators
age = 25
has_ticket = True
is_member = False

# VIP entry: must be adult AND (has ticket OR is member)
can_enter = age >= 18 and (has_ticket or is_member)
print(f"Can enter: {can_enter}")  # True


# Example 5 — Operator Precedence
# Order: not > and > or (like PEMDAS for logic)

result = True or True and False
# Evaluates as: True or (True and False) → True or False → True

result = not False and True or False
# Evaluates as: (not False) and True or False → True and True or False → True

print(f"Result: {result}")


# Example 6 — Practical Use Cases
# Check if a year is a leap year
year = 2024
is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
print(f"{year} is leap: {is_leap}")  # True

# Validate user input
username = "admin"
password = "secret123"
is_admin = True

login_success = (username == "admin" and password == "secret123") and is_admin
print(f"Login: {login_success}")


# ═══════════════════════════════════════════════════════════════════════════════
# PRACTICE EXERCISE
# ═══════════════════════════════════════════════════════════════════════════════
# 1. Create two boolean variables and combine them with `and`
# 2. Use `or` to check if a number is negative OR greater than 100
# 3. Use `not` to invert a boolean
# 4. Write a complex condition with parentheses to control order
# ═══════════════════════════════════════════════════════════════════════════════

# 1. Two booleans with `and`
has_car = True
has_gas = False
can_travel = has_car and has_gas
print(f"Can travel: {can_travel}")

# 2. `or` for range check
temp = -5
is_extreme = temp < 0 or temp > 100
print(f"Temperature is extreme: {is_extreme}")

# 3. Invert with `not`
is_logged_in = False
print(f"Not logged in: {not is_logged_in}")

# 4. Complex condition
age = 20
is_student = True
has_discount = (age < 25 or age > 65) and is_student
print(f"Has discount: {has_discount}")

# Try modifying it:
# - Check if a number is between 1-10, 20-30, or 40-50
num = 25
in_range = (1 <= num <= 10) or (20 <= num <= 30) or (40 <= num <= 50)
print(f"Number in special range: {in_range}")
