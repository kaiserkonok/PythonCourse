"""
Sets (Unique Collections)
────────────────────────────────────────────────────────────────────────────
Code examples and practice exercises from the lesson.
────────────────────────────────────────────────────────────────────────────
"""

# Example 1 — Removing Duplicates
numbers = [1, 2, 2, 3, 3, 4, 4, 5]

unique = list(set(numbers))
print(unique)  # [1, 2, 3, 4, 5] (order may vary)


# Example 2 — Union and Intersection
group_a = {"Alice", "Bob", "Charlie"}
group_b = {"Bob", "David", "Eve"}

# Everyone in either group
everyone = group_a | group_b
print(f"All: {everyone}")

# People in both groups
common = group_a & group_b
print(f"Common: {common}")


# Example 3 — Difference
all_users = {"Alice", "Bob", "Charlie", "David"}
active_users = {"Alice", "David"}

# Users who are not active
inactive = all_users - active_users
print(f"Inactive: {inactive}")  # {"Bob", "Charlie"}


# Example 4 — Symmetric Difference
list_a = {1, 2, 3, 4}
list_b = {3, 4, 5, 6}

# Items that appear in only one set
diff = list_a ^ list_b
print(f"Unique to each: {diff}")  # {1, 2, 5, 6}


# Example 5 — Membership Testing
# Sets are FAST for checking if something exists
valid_colors = {"red", "green", "blue"}

if "red" in valid_colors:
    print("Valid color!")

# Much faster than lists for large collections


# Example 6 — Frozen Sets
# Immutable sets (can be dictionary keys)
frozen = frozenset([1, 2, 3])

d = {frozen: "value"}
print(d[frozen])  # "value"


# ═══════════════════════════════════════════════════════════════════════════════
# PRACTICE EXERCISE
# ═══════════════════════════════════════════════════════════════════════════════
# 1. Create a set from a list with duplicates
# 2. Find common elements between two sets
# 3. Find elements in one set but not the other
# 4. Add and remove items from a set
# ═══════════════════════════════════════════════════════════════════════════════

# 1. Create set from list
raw_data = [10, 20, 20, 30, 30, 40]
unique_data = set(raw_data)
print(f"Unique: {unique_data}")

# 2. Common elements
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
common = set_a & set_b
print(f"Common: {common}")

# 3. Elements in one but not other
only_a = set_a - set_b
print(f"Only in A: {only_a}")

# 4. Add and remove
fruits = {"apple", "banana"}
fruits.add("cherry")
fruits.discard("banana")
print(f"Fruits: {fruits}")

# Try modifying it:
# - Check if two lists have any common elements
list1 = [1, 2, 3]
list2 = [3, 4, 5]
has_common = bool(set(list1) & set(list2))
print(f"Lists overlap: {has_common}")
