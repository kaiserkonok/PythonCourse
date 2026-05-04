"""
Loop Control (break, continue, else)
────────────────────────────────────────────────────────────────────────────
Code examples and practice exercises from the lesson.
────────────────────────────────────────────────────────────────────────────
"""

# Example 1 — `break` in a For Loop
# Search for a number
target = 7
numbers = [1, 3, 5, 7, 9, 11]

for num in numbers:
    if num == target:
        print(f"Found {target}!")
        break
    print(f"Checking {num}...")


# Example 2 — `break` in a While Loop
# Keep asking until user enters "quit"
# (Simulated to avoid blocking)
commands = ["run", "test", "quit"]
for command in commands:
    print(f"Enter command (or 'quit' to exit): {command}")
    if command == "quit":
        print("Goodbye!")
        break
    print(f"Running: {command}")


# Example 3 — `continue` in Action
# Process only odd numbers
for i in range(10):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(f"Processing {i}")


# Example 4 — `continue` to Skip Errors
# Process data, skip invalid entries
data = [10, 0, 20, 30]  # Removed "bad" to avoid TypeError in simple example

for item in data:
    try:
        result = 100 / item
        print(f"100 / {item} = {result}")
    except ZeroDivisionError:
        print(f"Skipping {item} (division by zero)")
        continue


# Example 5 — `else` with `break`
# Check if a number is prime
number = 17

for i in range(2, number):
    if number % i == 0:
        print(f"{number} is not prime (divisible by {i})")
        break
else:
    # Only runs if loop didn't break
    print(f"{number} is prime!")


# Example 6 — Combining All Three
# Process a list, skip negatives, stop at 999
numbers = [5, -2, 10, -8, 15, 999, 20]

for num in numbers:
    if num == 999:
        print("Found sentinel value, stopping!")
        break
    if num < 0:
        print(f"Skipping negative: {num}")
        continue
    print(f"Processing: {num}")
else:
    print("All numbers processed (no 999 found)")


# ═══════════════════════════════════════════════════════════════════════════════
# PRACTICE EXERCISE
# ═══════════════════════════════════════════════════════════════════════════════
# 1. Use break to stop a loop when you find a specific number
# 2. Use continue to skip numbers divisible by 3
# 3. Use else to detect if a search failed
# 4. Combine break and continue in one loop
# ═══════════════════════════════════════════════════════════════════════════════

# 1. Find specific number
search_list = [2, 5, 8, 12, 15, 20]
search_target = 12
for num in search_list:
    if num == search_target:
        print(f"Found {search_target}!")
        break
else:
    print(f"{search_target} not found")

# 2. Skip numbers divisible by 3
for i in range(1, 11):
    if i % 3 == 0:
        continue
    print(i, end=" ")
print()

# 3. Search with else
items = ["apple", "banana", "cherry"]
target = "grape"
for item in items:
    if item == target:
        print(f"Found {target}")
        break
else:
    print(f"{target} not in list")

# 4. Combine break and continue
values = [1, 2, -3, 4, 5, -6, 7, 99, 8]
for val in values:
    if val == 99:
        print("Found 99, stopping!")
        break
    if val < 0:
        print(f"Skip negative: {val}")
        continue
    print(f"Value: {val}")

# Try modifying it:
# - Use break in nested loops (note: only exits inner loop)
for row in range(3):
    for col in range(3):
        if row == 1 and col == 1:
            print("Breaking inner loop")
            break
        print(f"({row}, {col})")
