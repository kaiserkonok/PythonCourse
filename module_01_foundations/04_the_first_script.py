"""
The First Script
────────────────────────────────────────────────────────────────────────────
Code examples and practice exercises from the lesson.
────────────────────────────────────────────────────────────────────────────
"""

# Example 1 — Basic print()
# Simple text output
print("Hello, World!")


# Example 2 — Print Numbers
# No quotes needed for numbers
print(42)          # Output: 42
print(3.14159)     # Output: 3.14159
print(-100)        # Output: -100


# Example 3 — Print Calculations
# Python evaluates the math first
print(10 + 5)       # Output: 15
print(10 * 3)       # Output: 30
print(100 / 4)      # Output: 25.0


# Example 4 — Print Variables
# Store a value, then print it
message = "Learning Python!"
print(message)


# Example 5 — f-strings
name = "Alice"
age = 25
city = "New York"

print(f"My name is {name}")
print(f"I am {age} years old")
print(f"I live in {city}")
print(f"Next year I'll be {age + 1}")


# Example 6 — Customizing print()
# end parameter — no newline
print("Hello", end=" ")
print("World")

# sep parameter — custom separator
print("Python", "is", "fun", sep="-")

# Both together
print("A", "B", "C", sep=" → ", end="!\n")


# Example 7 — Common Mistakes to Avoid
# ❌ print(Hello)  → NameError (Hello is not a variable)
# ✅ print("Hello")  → Correct

# ❌ print(x) before x = 10  → NameError
# ✅ x = 10; print(x)  → Correct

# ❌ print("5" + "5")  → "55" (string concatenation, not math)
# ✅ print(5 + 5)  → 10 (addition)


# ═══════════════════════════════════════════════════════════════════════════════
# PRACTICE EXERCISE
# ═══════════════════════════════════════════════════════════════════════════════
# Create a script that:
# 1. Creates 3 variables: your name, your age, your city
# 2. Prints each on a separate line
# 3. Uses an f-string to show what your age will be in 10 years
#
# Expected output:
#   My name is Alice
#   My age is 25
#   I live in New York
#   In 10 years, I will be 35
# ═══════════════════════════════════════════════════════════════════════════════

my_name = "Alice"
my_age = 25
my_city = "New York"

print(f"My name is {my_name}")
print(f"My age is {my_age}")
print(f"I live in {my_city}")
print(f"In 10 years, I will be {my_age + 10}")

# Try modifying it:
# - Change the values
# - Add a hobby variable
# - Calculate how old you'll be in 20 years
my_hobby = "reading"
print(f"My hobby is {my_hobby}")
print(f"In 20 years, I will be {my_age + 20}")