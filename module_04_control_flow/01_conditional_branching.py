"""
Conditional Branching (Making Decisions)
────────────────────────────────────────────────────────────────────────────
Code examples and practice exercises from the lesson.
────────────────────────────────────────────────────────────────────────────
"""

# Example 1 — Simple `if`
age = 20

if age >= 18:
    print("You are an adult")
    print("You can vote")

print("This always runs")


# Example 2 — `if/else`
temperature = 30

if temperature > 25:
    print("It's warm outside")
else:
    print("It's cold outside")


# Example 3 — `if/elif/else`
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Grade: {grade}")  # B


# Example 4 — Nested Conditions
age = 25
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("Bring ID")
else:
    print("Too young")


# Example 5 — Multiple Conditions
age = 25
is_student = True

# AND
if age < 30 and is_student:
    print("Student discount available")

# OR
if age < 18 or age > 65:
    print("Special pricing")


# Example 6 — Ternary Operator (One-Liner)
# Traditional
age = 20
if age >= 18:
    status = "adult"
else:
    status = "minor"

# One-liner
status = "adult" if age >= 18 else "minor"
print(f"Status: {status}")  # adult


# ═══════════════════════════════════════════════════════════════════════════════
# PRACTICE EXERCISE
# ═══════════════════════════════════════════════════════════════════════════════
# 1. Write an if/else to check if a number is even or odd
# 2. Use if/elif/else to categorize age: child (0-12), teen (13-19), adult (20-64), senior (65+)
# 3. Write a nested if to check if a number is positive, and if so, whether it's > 10
# 4. Convert an if/else to a ternary operator
# ═══════════════════════════════════════════════════════════════════════════════

# 1. Even or odd
num = 15
if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")

# 2. Age category
person_age = 30
if person_age <= 12:
    category = "child"
elif person_age <= 19:
    category = "teen"
elif person_age <= 64:
    category = "adult"
else:
    category = "senior"
print(f"Category: {category}")

# 3. Nested if
x = 15
if x > 0:
    print("Positive")
    if x > 10:
        print("Greater than 10")
    else:
        print("Less than or equal to 10")
else:
    print("Non-positive")

# 4. Ternary operator
temperature = 30
weather = "warm" if temperature > 25 else "cold"
print(f"Weather: {weather}")

# Try modifying it:
# - Add validation for negative age
age_input = -5
if age_input < 0:
    print("Invalid age!")
elif age_input <= 12:
    print("Child")
elif age_input <= 19:
    print("Teen")
elif age_input <= 64:
    print("Adult")
else:
    print("Senior")
