"""
Generators & Iterators (Lazy Evaluation)
────────────────────────────────────────────────────────────────────────────
Code examples and practice exercises from the lesson.
────────────────────────────────────────────────────────────────────────────
"""

# Example 1 — Basic Generator
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for num in countdown(5):
    print(num)  # 5, 4, 3, 2, 1


# Example 2 — Generator Expression
# List comprehension (eager)
squares_list = [x**2 for x in range(5)]
print(squares_list)  # [0, 1, 4, 9, 16]

# Generator expression (lazy)
squares_gen = (x**2 for x in range(5))
print(next(squares_gen))  # 0
print(next(squares_gen))  # 1


# Example 3 — Memory Efficiency
import sys

# List — stores all 1M items
big_list = [x for x in range(100_000)]
print(f"List: {sys.getsizeof(big_list)} bytes")

# Generator — stores only state
big_gen = (x for x in range(100_000))
print(f"Generator: {sys.getsizeof(big_gen)} bytes")


# Example 4 — Infinite Generator
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Get first 10 fibonacci numbers
fib = fibonacci()
for _ in range(10):
    print(next(fib), end=" ")
print()


# Example 5 — Pipeline with Generators
def read_data():
    for i in range(1, 6):
        yield i

def filter_odd(data):
    for item in data:
        if item % 2 == 1:
            yield item

def double(data):
    for item in data:
        yield item * 2

# Chain generators
pipeline = double(filter_odd(read_data()))
print(list(pipeline))  # [2, 6, 10]


# Example 6 — `yield from`
def chain(*iterables):
    for it in iterables:
        yield from it

result = list(chain([1, 2], [3, 4], [5, 6]))
print(result)  # [1, 2, 3, 4, 5, 6]


# ═══════════════════════════════════════════════════════════════════════════════
# PRACTICE EXERCISE
# ═══════════════════════════════════════════════════════════════════════════════
# 1. Create a generator that yields even numbers up to n
# 2. Use a generator expression to sum squares of 1-100
# 3. Create a generator that yields prime numbers
# 4. Chain two generators together
# ═══════════════════════════════════════════════════════════════════════════════

# 1. Even numbers generator
def evens_up_to(n):
    for i in range(2, n + 1, 2):
        yield i

print(f"Evens: {list(evens_up_to(10))}")

# 2. Sum squares with generator
total = sum(x**2 for x in range(1, 101))
print(f"Sum of squares: {total}")

# 3. Prime numbers generator
def primes():
    found = []
    num = 2
    while True:
        if all(num % p != 0 for p in found):
            found.append(num)
            yield num
        num += 1

prime_gen = primes()
for _ in range(10):
    print(next(prime_gen), end=" ")
print()

# 4. Chain generators
def multiply_by(data, factor):
    for item in data:
        yield item * factor

def add_offset(data, offset):
    for item in data:
        yield item + offset

pipeline2 = add_offset(multiply_by(range(1, 4), 10), 5)
print(f"Pipeline: {list(pipeline2)}")  # [15, 25, 35]

# Try modifying it:
# - Generator that reads a file line by line (memory efficient)
import os

def read_lines(filepath):
    with open(filepath, "w") as f:
        f.write("Line 1\nLine 2\nLine 3\n")

    with open(filepath, "r") as f:
        for line in f:
            yield line.strip()

for line in read_lines("gen_test.txt"):
    print(f"  {line}")

os.remove("gen_test.txt")
