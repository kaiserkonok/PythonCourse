"""
Variables & Memory Labels
────────────────────────────────────────────────────────────────────────────
Code examples and practice exercises from the lesson.
────────────────────────────────────────────────────────────────────────────
"""

# Example 1 — Creating Variables
# Create a variable and print it
player_name = "Mario"
print(player_name)  # Output: Mario


# Example 2 — Reassigning Variables
# Variables can change their value
age = 25
print(age)       # 25

age = 26          # Reassign the variable
print(age)       # 26 (old value is gone)


# Example 3 — Multiple Variables
# Multiple variables in one script
x = 5
y = 10
z = x + y
print(z)  # Output: 15


# Example 4 — Multiple Assignment
# Python lets you assign multiple variables at once
a, b, c = 1, 2, 3
print(a, b, c)  # 1 2 3

# Swap values (Python magic!)
x = 10
y = 20
x, y = y, x      # No temp variable needed
print(f"x = {x}, y = {y}")  # x = 20, y = 10


# Example 5 — Checking a Variable's Type
# Every variable has a type — Python tracks it for you
age = 25
name = "Alice"
is_student = True

print(type(age))        # <class 'int'>
print(type(name))       # <class 'str'>
print(type(is_student))  # <class 'bool'>


# ═══════════════════════════════════════════════════════════════════════════════
# PRACTICE EXERCISE
# ═══════════════════════════════════════════════════════════════════════════════
# Create variables for:
# 1. Your first name (string)
# 2. Your last name (string)
# 3. Your age (integer)
# 4. Whether you like programming (boolean)
#
# Print them all on one line using an f-string.
# ═══════════════════════════════════════════════════════════════════════════════

first_name = "Alice"
last_name = "Smith"
my_age = 25
likes_programming = True

print(f"{first_name} {last_name}, age {my_age}, likes programming: {likes_programming}")

# Try modifying it:
# - Change the values
# - Add a city variable
# - Print on separate lines
my_city = "New York"
print(f"\nCity: {my_city}")
print(f"First name: {first_name}")
print(f"Last name: {last_name}")