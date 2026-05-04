# 🧺 Sets: Unique Collections

<p align="center">
  <img src="https://img.shields.io/badge/set-Unique%20Items-blue?style=flat-square" alt="set">
  <img src="https://img.shields.io/badge/Math-Union%2FIntersect-green?style=flat-square" alt="Math">
  <img src="https://img.shields.io/badge/Fast-Membership%20Test-orange?style=flat-square" alt="Fast">
</p>

> ### 💡 Sets are like a basket that only holds unique items. Drop in a duplicate, and it disappears. Perfect for removing duplicates and math operations.
> Learn how to work with collections of unique items.

---

## 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- ✅ Create and manipulate sets
- ✅ Use set operations: union, intersection, difference
- ✅ Remove duplicates from lists using sets

---

## 🧠 Mental Model: A VIP Guest List

A set is a **collection of unique items**. Think of it like a VIP guest list:

```
[Alice] [Bob] [Charlie] [Alice]  ← Duplicate Alice is ignored!
```

No order, no duplicates. Just unique items.

---

## 📖 Creating Sets

```python
# Empty set (must use set(), {} creates a dict)
empty = set()

# Basic set
fruits = {"apple", "banana", "cherry"}

# From a list (removes duplicates)
numbers = set([1, 2, 2, 3, 3, 4])
print(numbers)  # {1, 2, 3, 4}
```

---

## 🔄 Set Operations

Sets support **mathematical set operations**:

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Union — all items from both
a | b  # {1, 2, 3, 4, 5, 6}

# Intersection — only items in both
a & b  # {3, 4}

# Difference — items in a but not b
a - b  # {1, 2}

# Symmetric difference — items in either, but not both
a ^ b  # {1, 2, 5, 6}
```

---

## ⚙️ Modifying Sets

```python
s = {1, 2, 3}

s.add(4)        # {1, 2, 3, 4}
s.remove(2)     # {1, 3, 4}
s.discard(99)   # Safe remove (no error if missing)
s.clear()       # Empty the set
```

---

## ⚠️ Common Mistakes

```
❌ Creating empty sets
   s = {}    → This is a dictionary!
   s = set() ← Correct way to create empty set

❌ Assuming order
   s = {3, 1, 2}
   for x in s:  → Order is not guaranteed!

❌ Using mutable items in sets
   s = {[1, 2]}  → TypeError
   Sets only hold immutable items (like tuples)

❌ Forgetting set operations
   # Manual duplicate removal
   seen = []
   for x in items:
       if x not in seen:
           seen.append(x)

   # Pythonic
   unique = list(set(items))
```

---

## 💻 Code Examples

### 📌 Example 1 — Removing Duplicates

```python
numbers = [1, 2, 2, 3, 3, 4, 4, 5]

unique = list(set(numbers))
print(unique)  # [1, 2, 3, 4, 5] (order may vary)
```

### 📌 Example 2 — Union and Intersection

```python
group_a = {"Alice", "Bob", "Charlie"}
group_b = {"Bob", "David", "Eve"}

# Everyone in either group
everyone = group_a | group_b
print(f"All: {everyone}")

# People in both groups
common = group_a & group_b
print(f"Common: {common}")
```

### 📌 Example 3 — Difference

```python
all_users = {"Alice", "Bob", "Charlie", "David"}
active_users = {"Alice", "David"}

# Users who are not active
inactive = all_users - active_users
print(f"Inactive: {inactive}")  # {"Bob", "Charlie"}
```

### 📌 Example 4 — Symmetric Difference

```python
list_a = {1, 2, 3, 4}
list_b = {3, 4, 5, 6}

# Items that appear in only one set
diff = list_a ^ list_b
print(f"Unique to each: {diff}")  # {1, 2, 5, 6}
```

### 📌 Example 5 — Membership Testing

```python
# Sets are FAST for checking if something exists
valid_colors = {"red", "green", "blue"}

if "red" in valid_colors:
    print("Valid color!")

# Much faster than lists for large collections
```

### 📌 Example 6 — Frozen Sets

```python
# Immutable sets (can be dictionary keys)
frozen = frozenset([1, 2, 3])

d = {frozen: "value"}
print(d[frozen])  # "value"
```

---

## 🧪 Practice Exercise

1. Create a set from a list with duplicates
2. Find common elements between two sets
3. Find elements in one set but not the other
4. Add and remove items from a set

---

## 📋 Key Takeaways

| Concept | Takeaway |
|---------|----------|
| 🧺 **Unique** | Sets automatically remove duplicates |
| 🔄 **Operations** | `|` (union), `&` (intersection), `-` (difference), `^` (symmetric diff) |
| ⚡ **Fast** | Membership testing (`x in s`) is very fast |
| 🔒 **Unordered** | Sets don't guarantee item order |
| 📦 **Use case** | Deduplication, math operations, membership checks |

---

## 🔗 Further Reading

- 📖 [Sets — Official Docs](https://docs.python.org/3/tutorial/datastructures.html#sets)
- 🧮 [Set Operations — docs](https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset)
- 🌐 [Sets vs Lists — Real Python](https://realpython.com/python-sets/)