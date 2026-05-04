"""
Lists (Your Data Backpack)
────────────────────────────────────────────────────────────────────────────
Code examples and practice exercises from the lesson.
────────────────────────────────────────────────────────────────────────────
"""

# Example 1 — Basic List Operations
numbers = [10, 20, 30]

# Access
print(numbers[0])  # 10

# Modify
numbers[1] = 25
print(numbers)     # [10, 25, 30]

# Add
numbers.append(40)
print(numbers)     # [10, 25, 30, 40]


# Example 2 — Insert and Remove
fruits = ["apple", "cherry"]

fruits.insert(1, "banana")
print(fruits)  # ["apple", "banana", "cherry"]

fruits.remove("cherry")
print(fruits)  # ["apple", "banana"]

last = fruits.pop()
print(f"Popped: {last}, List: {fruits}")


# Example 3 — Sorting and Reversing
scores = [85, 92, 78, 90, 88]

scores.sort()
print(f"Ascending: {scores}")  # [78, 85, 88, 90, 92]

scores.reverse()
print(f"Descending: {scores}")  # [92, 90, 88, 85, 78]


# Example 4 — Slicing Lists
letters = ['a', 'b', 'c', 'd', 'e']

print(letters[:3])    # ['a', 'b', 'c'] (first 3)
print(letters[2:])    # ['c', 'd', 'e'] (from index 2)
print(letters[::2])   # ['a', 'c', 'e'] (every 2nd)
print(letters[::-1])  # ['e', 'd', 'c', 'b', 'a'] (reverse)


# Example 5 — Checking Membership
colors = ["red", "green", "blue"]

if "red" in colors:
    print("Found red!")

print(len(colors))    # 3 (length)
print(colors.count("green"))  # 1


# Example 6 — Copying Lists
original = [1, 2, 3]

# Alias (dangerous)
alias = original
alias[0] = 99
print(original)  # [99, 2, 3] — changed!

# Safe copy
safe_copy = original.copy()
safe_copy[0] = 1
print(original)  # [99, 2, 3] — unchanged


# ═══════════════════════════════════════════════════════════════════════════════
# PRACTICE EXERCISE
# ═══════════════════════════════════════════════════════════════════════════════
# 1. Create a list of your 5 favorite movies
# 2. Add a new movie to the end
# 3. Remove the first movie
# 4. Sort the list alphabetically
# 5. Print the reversed list
# ═══════════════════════════════════════════════════════════════════════════════

# 1. Create list
movies = ["Inception", "The Matrix", "Interstellar", "Avatar", "Titanic"]

# 2. Add new movie
movies.append("Dune")
print(f"Added Dune: {movies}")

# 3. Remove first movie
removed = movies.pop(0)
print(f"Removed {removed}: {movies}")

# 4. Sort alphabetically
movies.sort()
print(f"Sorted: {movies}")

# 5. Reverse
movies.reverse()
print(f"Reversed: {movies}")

# Try modifying it:
# - Create a list of lists (nested)
grades = [[90, 85, 88], [75, 80, 82], [95, 92, 98]]
print(f"Student 2 average: {sum(grades[1]) / len(grades[1])}")
