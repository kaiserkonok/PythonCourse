"""
Lambda Functions (Anonymous One-Liners)
────────────────────────────────────────────────────────────────────────────
Code examples and practice exercises from the lesson.
────────────────────────────────────────────────────────────────────────────
"""

# Example 1 — Basic Lambda
# Regular function
def square(x):
    return x ** 2

# Lambda equivalent
square = lambda x: x ** 2

print(square(5))  # 25


# Example 2 — Multiple Arguments
add = lambda a, b: a + b
print(add(3, 4))  # 7


# Example 3 — Sorting with Lambda
students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92},
    {"name": "Charlie", "grade": 78}
]

# Sort by grade
sorted_students = sorted(students, key=lambda s: s["grade"])
print(sorted_students)


# Example 4 — `map()` with Lambda
numbers = [1, 2, 3, 4, 5]

# Square each number
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # [1, 4, 9, 16, 25]


# Example 5 — `filter()` with Lambda
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Keep only even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4, 6, 8, 10]


# Example 6 — Immediate Invocation
# Lambda called immediately
result = (lambda x, y: x + y)(3, 4)
print(result)  # 7


# ═══════════════════════════════════════════════════════════════════════════════
# PRACTICE EXERCISE
# ═══════════════════════════════════════════════════════════════════════════════
# 1. Create a lambda that multiplies two numbers
# 2. Use a lambda to sort a list of tuples by the second element
# 3. Filter a list of words to only include those longer than 5 characters
# 4. Use map() with a lambda to convert strings to uppercase
# ═══════════════════════════════════════════════════════════════════════════════

# 1. Multiply lambda
multiply = lambda a, b: a * b
print(f"3 * 4 = {multiply(3, 4)}")

# 2. Sort tuples by second element
pairs = [(1, 5), (3, 2), (2, 8), (4, 1)]
sorted_pairs = sorted(pairs, key=lambda p: p[1])
print(f"Sorted: {sorted_pairs}")

# 3. Filter long words
words = ["apple", "banana", "cherry", "fig", "watermelon"]
long_words = list(filter(lambda w: len(w) > 5, words))
print(f"Long words: {long_words}")

# 4. Map to uppercase
texts = ["hello", "world", "python"]
upper_texts = list(map(lambda t: t.upper(), texts))
print(f"Upper: {upper_texts}")

# Try modifying it:
# - Use lambda with reduce to sum a list
from functools import reduce
numbers = [1, 2, 3, 4, 5]
total = reduce(lambda a, b: a + b, numbers)
print(f"Total: {total}")
