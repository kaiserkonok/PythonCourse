"""
Strings (Text Processing)
────────────────────────────────────────────────────────────────────────────
Code examples and practice exercises from the lesson.
────────────────────────────────────────────────────────────────────────────
"""

# Example 1 — Basic String
greeting = "Hello, World!"
print(greeting)


# Example 2 — String Length
message = "Python"
print(len(message))  # 6


# Example 3 — String Concatenation & Repetition
# Combine strings with +
first = "Hello"
second = "World"
print(first + " " + second)  # Hello World

# Repeat strings with *
echo = "Ha" * 3
print(echo)  # HaHaHa


# Example 4 — Indexing
word = "Python"

print(word[0])    # P (first)
print(word[1])    # y (second)
print(word[-1])   # n (last)
print(word[-2])   # o (second to last)


# Example 5 — Slicing
language = "Python"

print(language[0:3])   # "Pyt"
print(language[1:4])   # "yth"
print(language[:3])    # "Pyt" (same as [0:3])
print(language[3:])    # "hon" (from 3 to end)
print(language[::-1])  # "nohtyP" (reverse)


# Example 6 — String Methods
text = "  Hello, Python!  "

# Transform
print(text.strip())           # "Hello, Python!"
print(text.upper())           # "  HELLO, PYTHON!  "
print(text.lower())           # "  hello, python!  "
print(text.title())           # "  Hello, Python!  "

# Search and replace
print(text.replace("Python", "World"))  # "  Hello, World!  "
print("hello" in text.lower())           # True


# Example 7 — f-strings (Review from Module 1)
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old.")


# ═══════════════════════════════════════════════════════════════════════════════
# PRACTICE EXERCISE
# ═══════════════════════════════════════════════════════════════════════════════
# 1. Create a string with your full name
# 2. Print just your first name (using slicing)
# 3. Print the length of your name
# 4. Convert your name to uppercase
# 5. Create an f-string combining your name and age
# ═══════════════════════════════════════════════════════════════════════════════

full_name = "Alice Smith"

# 1. Print just the first name (using slicing)
first_name = full_name[:5]  # "Alice"
print(f"First name: {first_name}")

# 2. Print the length of your name
print(f"Length: {len(full_name)}")

# 3. Convert your name to uppercase
print(f"Uppercase: {full_name.upper()}")

# 4. Create an f-string combining your name and age
age = 25
print(f"My name is {full_name} and I am {age} years old.")

# Try modifying it:
# - Extract the last name instead of first name
last_name = full_name[6:]
print(f"Last name: {last_name}")
# - Find the position of the space
space_position = full_name.find(" ")
print(f"Space is at position: {space_position}")