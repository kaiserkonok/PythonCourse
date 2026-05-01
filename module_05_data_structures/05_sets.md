# Sets: Mathematical Collections and Removing Duplicates

## Learning Objectives

- Create and use sets
- Understand set operations
- Remove duplicates efficiently

## What is a Set?

A set is an **unordered collection** with **no duplicates**:

- Unordered: No specific order
- Unique: No duplicate items
- Fast membership checking

```python
fruits = {"apple", "banana", "cherry", "apple"}
print(fruits)  # {'apple', 'banana', 'cherry'} - duplicates removed!
```

## Creating Sets

```python
# Standard set
colors = {"red", "green", "blue"}

# Using set() function
vowels = set("aeiouaaeiou")  # {'a', 'e', 'i', 'o', 'u'}

# Empty set (NOT {} - that's a dict!)
empty = set()
```

## Set Operations

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Union (all elements)
print(a | b)          # {1, 2, 3, 4, 5, 6}
# or
print(a.union(b))

# Intersection (common elements)
print(a & b)          # {3, 4}
print(a.intersection(b))

# Difference (in a but not b)
print(a - b)          # {1, 2}
print(a.difference(b))

# Symmetric difference (not in both)
print(a ^ b)          # {1, 2, 5, 6}
print(a.symmetric_difference(b))
```

## Membership Checking

```python
fruits = {"apple", "banana", "cherry"}

print("apple" in fruits)      # True
print("orange" in fruits)    # False
```

## Code Examples

```python
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
```

## When to Use Sets

| Use Case | Why |
|---------|-----|
| Remove duplicates | Easy way to get unique items |
| Membership checking | Very fast O(1) |
| Mathematical operations | Union, intersection, difference |
| Remove duplicates from list | set(list) |

## Key Takeaways

1. **Sets use {}** but no key-value pairs
2. **No duplicates** - automatically removed
3. **Unordered** - no index access
4. **Fast operations** - union, intersection
5. **Use for** - unique items, membership tests

## Practice Exercise

1. Create a set from a list with duplicates
2. Find common elements between two sets
3. Find elements in set1 but not set2
4. Check if one set is a subset of another