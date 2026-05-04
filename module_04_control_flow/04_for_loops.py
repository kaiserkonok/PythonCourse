"""
For Loops (Iterating Over Sequences)
────────────────────────────────────────────────────────────────────────────
Code examples and practice exercises from the lesson.
────────────────────────────────────────────────────────────────────────────
"""

# Example 1 — Loop Over a List
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(f"I like {fruit}")


# Example 2 — Loop Over a String
word = "Python"

for char in word:
    print(char)
# P
# y
# t
# h
# o
# n


# Example 3 — Using `range()`
# range(stop) — 0 to stop-1
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

print("---")

# range(start, stop)
for i in range(2, 6):
    print(i)  # 2, 3, 4, 5

print("---")

# range(start, stop, step)
for i in range(0, 10, 2):
    print(i)  # 0, 2, 4, 6, 8


# Example 4 — `enumerate()` — Index + Value
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
# 0: apple
# 1: banana
# 2: cherry


# Example 5 — `zip()` — Loop Over Two Lists
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

for name, age in zip(names, ages):
    print(f"{name} is {age} years old")


# Example 6 — Nested For Loops
# Multiplication table
for row in range(1, 4):
    for col in range(1, 4):
        print(f"{row} x {col} = {row * col}", end="\t")
    print()  # New line after each row


# ═══════════════════════════════════════════════════════════════════════════════
# PRACTICE EXERCISE
# ═══════════════════════════════════════════════════════════════════════════════
# 1. Loop over a list of your favorite foods and print each
# 2. Use range() to print numbers from 10 down to 1
# 3. Use enumerate() to print a numbered list
# 4. Use zip() to combine two lists into pairs
# ═══════════════════════════════════════════════════════════════════════════════

# 1. Favorite foods
foods = ["pizza", "sushi", "tacos"]
for food in foods:
    print(f"Love {food}!")

# 2. Countdown from 10 to 1
for i in range(10, 0, -1):
    print(i)
print("Blastoff!")

# 3. Enumerate numbered list
items = ["apples", "bananas", "cherries"]
for i, item in enumerate(items, 1):
    print(f"{i}. {item}")

# 4. Zip two lists
colors = ["red", "green", "blue"]
shapes = ["circle", "square", "triangle"]
for color, shape in zip(colors, shapes):
    print(f"{color} {shape}")

# Try modifying it:
# - Calculate the sum of a list using a for loop
numbers = [1, 2, 3, 4, 5]
total = 0
for num in numbers:
    total += num
print(f"Sum: {total}")
