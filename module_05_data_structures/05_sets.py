# Code examples from "Sets" lesson

# Example 1: Create and access
numbers = {1, 2, 3, 2, 1}
print(numbers)  # {1, 2, 3} - duplicates removed

# Example 2: Add/remove elements
fruits = {"apple"}
fruits.add("banana")
fruits.add("cherry")
print(fruits)  # {'apple', 'banana', 'cherry'}

fruits.remove("apple")
print(fruits)  # {'banana', 'cherry'}

# Example 3: Set operations
x = {1, 2, 3}
y = {3, 4, 5}

print(f"Union: {x | y}")         # {1, 2, 3, 4, 5}
print(f"Intersection: {x & y}")  # {3}
print(f"Difference: {x - y}")      # {1, 2}

# Example 4: Remove duplicates from list
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 5]
unique = set(numbers)
print(unique)  # {1, 2, 3, 4, 5}
# Convert back to list if needed
unique_list = list(set(numbers))
print(unique_list)  # [1, 2, 3, 4, 5] (order may vary)

# Example 5: Subset checking
a = {1, 2, 3}
b = {1, 2, 3, 4, 5}
print(a.issubset(b))  # True
print(b.issuperset(a))  # True


# =====================
# PRACTICE EXERCISE
# =====================

# 1. Create a set from a list with duplicates
data = [1, 2, 2, 3, 3, 3, 4, 5, 5]
unique_set = set(data)
print(f"Unique: {unique_set}")

# 2. Find common elements between two sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
common = set1 & set2
print(f"Common: {common}")

# 3. Find elements in set1 but not set2
diff = set1 - set2
print(f"In set1 but not set2: {diff}")

# 4. Check if one set is a subset of another
small = {1, 2}
large = {1, 2, 3, 4, 5}
print(f"small is subset of large: {small.issubset(large)}")