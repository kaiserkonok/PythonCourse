# Code examples from "Booleans" lesson

# Example 1: Basic boolean
is_raining = True
print(f"Is it raining? {is_raining}")

# Example 2: Boolean operators
is_sunny = True
is_warm = False
print(is_sunny and is_warm)   # False (both must be True)
print(is_sunny or is_warm)    # True (at least one is True)
print(not is_sunny)          # False (opposite)

# Example 3: Comparison to boolean
score = 85
passed = score >= 60
print(f"Passed: {passed}")  # True

# Example 4: Multiple comparisons
age = 25
has_license = True
can_drive = age >= 18 and has_license
print(f"Can drive: {can_drive}")  # True

# Example 5: Boolean from string methods
email = "user@example.com"
is_valid = "@" in email
print(f"Valid email: {is_valid}")  # True


# =====================
# PRACTICE EXERCISE
# =====================

# 1. Create two boolean variables:
has_python_book = True
has_experience = False

# 2. Print whether you have both
print(f"Has both: {has_python_book and has_experience}")

# 3. Print whether you have at least one
print(f"Has at least one: {has_python_book or has_experience}")

# 4. Print the opposite of has_experience
print(f"Not has_experience: {not has_experience}")