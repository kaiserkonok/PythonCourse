"""
List Comprehensions (Python's Magic Syntax)
────────────────────────────────────────────────────────────────────────────
Code examples and practice exercises from the lesson.
────────────────────────────────────────────────────────────────────────────
"""

# Example 1 — Basic Comprehension
numbers = [1, 2, 3, 4, 5]

# Traditional loop
squares = []
for n in numbers:
    squares.append(n ** 2)

# Comprehension (same result, cleaner)
squares = [n ** 2 for n in numbers]
print(squares)  # [1, 4, 9, 16, 25]


# Example 2 — With a Condition
numbers = range(10)

# Only even numbers
evens = [n for n in numbers if n % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8]


# Example 3 — Transforming Strings
words = ["hello", "WORLD", "Python"]

# Uppercase all words
upper = [w.upper() for w in words]
print(upper)  # ["HELLO", "WORLD", "PYTHON"]

# Length of each word
lengths = [len(w) for w in words]
print(lengths)  # [5, 5, 6]


# Example 4 — If/Else in Comprehension
numbers = [1, 2, 3, 4, 5]

# Label even/odd
labels = ["even" if n % 2 == 0 else "odd" for n in numbers]
print(labels)  # ["odd", "even", "odd", "even", "odd"]


# Example 5 — Nested Comprehensions
# Flattening a matrix
matrix = [[1, 2], [3, 4], [5, 6]]

flat = [num for row in matrix for num in row]
print(flat)  # [1, 2, 3, 4, 5, 6]


# Example 6 — Dictionary Comprehension
# You can also create dicts!
numbers = [1, 2, 3, 4]

squares_dict = {n: n**2 for n in numbers}
print(squares_dict)  # {1: 1, 2: 4, 3: 9, 4: 16}


# ═══════════════════════════════════════════════════════════════════════════════
# PRACTICE EXERCISE
# ═══════════════════════════════════════════════════════════════════════════════
# 1. Create a list of squares from 1 to 10 using a comprehension
# 2. Filter a list of names to only include those starting with "A"
# 3. Convert a list of Celsius temperatures to Fahrenheit
# 4. Create a dictionary of numbers and their squares
# ═══════════════════════════════════════════════════════════════════════════════

# 1. Squares 1-10
squares_10 = [x**2 for x in range(1, 11)]
print(f"Squares: {squares_10}")

# 2. Names starting with "A"
names = ["Alice", "Bob", "Anna", "Charlie", "Amy"]
a_names = [name for name in names if name.startswith("A")]
print(f"A names: {a_names}")

# 3. Celsius to Fahrenheit
celsius = [0, 10, 20, 30, 40]
fahrenheit = [(c * 9/5) + 32 for c in celsius]
print(f"Fahrenheit: {fahrenheit}")

# 4. Dictionary of squares
nums = [1, 2, 3, 4, 5]
sq_dict = {n: n**2 for n in nums}
print(f"Dict: {sq_dict}")

# Try modifying it:
# - Create a 2D grid using nested comprehensions
grid = [[row * col for col in range(1, 4)] for row in range(1, 4)]
print(f"Grid: {grid}")
