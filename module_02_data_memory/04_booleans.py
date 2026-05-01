"""
Booleans (True/False Logic)
────────────────────────────────────────────────────────────────────────────
Code examples and practice exercises from the lesson.
────────────────────────────────────────────────────────────────────────────
"""

# Example 1 — Basic Boolean
is_raining = True
print(f"Is it raining? {is_raining}")


# Example 2 — Boolean from Comparison
age = 18
is_adult = age >= 18
print(f"Is adult: {is_adult}")


# Example 3 — Boolean Operators
is_sunny = True
is_warm = False

# AND — both must be True
print(is_sunny and is_warm)   # False

# OR — at least one must be True
print(is_sunny or is_warm)    # True

# NOT — inverts the value
print(not is_sunny)           # False


# Example 4 — Combining Conditions
age = 25
has_license = True

# Can drive if both conditions are True
can_drive = age >= 18 and has_license
print(f"Can drive: {can_drive}")


# Example 5 — Boolean from String Operations
email = "user@example.com"

# Check if email contains "@"
is_valid_email = "@" in email
print(f"Valid email: {is_valid_email}")

# Check if name is empty
name = ""
is_empty = not name
print(f"Name is empty: {is_empty}")


# Example 6 — Truthy and Falsy
# Check truthiness
print(bool(0))        # False
print(bool(1))        # True
print(bool(-1))       # True (any non-zero is True)
print(bool(""))       # False
print(bool("hello"))  # True


# Example 7 — Boolean Best Practices
# ❌ Not Pythonic
is_raining = True
if is_raining == True:
    print("Bring an umbrella")

# ✅ Pythonic
if is_raining:
    print("Bring an umbrella")


# ═══════════════════════════════════════════════════════════════════════════════
# PRACTICE EXERCISE
# ═══════════════════════════════════════════════════════════════════════════════
# 1. Create two boolean variables:
#    - has_python_book (True or False)
#    - has_experience (True or False)
# 2. Print whether you have both
# 3. Print whether you have at least one
# 4. Print the opposite of has_experience
# ═══════════════════════════════════════════════════════════════════════════════

has_python_book = True
has_experience = False

# 2. Print whether you have both
print(f"Has both: {has_python_book and has_experience}")

# 3. Print whether you have at least one
print(f"Has at least one: {has_python_book or has_experience}")

# 4. Print the opposite of has_experience
print(f"Not has_experience: {not has_experience}")

# Try modifying it:
# - Create a third boolean and combine all three
is_enrolled = True
can_start_course = has_python_book and has_experience and is_enrolled
print(f"Can start course: {can_start_course}")