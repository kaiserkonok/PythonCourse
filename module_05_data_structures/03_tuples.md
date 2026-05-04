# 🔒 Tuples: The Immutable Lists

<p align="center">
  <img src="https://img.shields.io/badge/tuple-Immutable%20List-blue?style=flat-square" alt="tuple">
  <img src="https://img.shields.io/badge/Fast-Optimized-green?style=flat-square" alt="fast">
  <img src="https://img.shields.io/badge/Safe-Data%20Integrity-orange?style=flat-square" alt="safe">
</p>

> ### 💡 Tuples are like lists that can't change. Once created, they stay the same — making them fast and safe for fixed data.
> Learn when to use tuples instead of lists.

---

## 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- ✅ Create and access tuples
- ✅ Understand the difference between lists and tuples
- ✅ Use tuple unpacking to assign multiple variables at once

---

## 🧠 Mental Model: A Sealed Envelope

A tuple is a **fixed collection**. Think of it like a sealed envelope:

```
(📍 Location) (📅 Date) (👤 Person)
  0             1         2
```

Once sealed, you **can't change** what's inside. This makes it fast and safe.

---

## 📖 Creating Tuples

```python
# Empty tuple
empty = ()

# Tuple of numbers
point = (10, 20)

# Mixed types
record = ("Alice", 25, "Engineer")

# Parentheses are optional (but recommended)
colors = "red", "green", "blue"  # Still a tuple!
```

> 💡 Tuples are defined by **commas**, not parentheses. `(1)` is an int, `(1,)` is a tuple.

---

## 🔑 Tuple Unpacking

Python lets you "unpack" tuples into variables:

```python
point = (10, 20)
x, y = point  # x = 10, y = 20

# Swap values (no temp variable needed)
a, b = b, a
```

---

## ⚖️ Lists vs Tuples

| Feature | 📦 List `[]` | 🔒 Tuple `()` |
|---------|-------------|--------------|
| **Mutable?** | ✅ Yes | ❌ No |
| **Speed** | Slower | ⚡ Faster |
| **Use for** | Changing data | Fixed data |
| **Dictionary keys?** | ❌ No | ✅ Yes |

---

## ⚠️ Common Mistakes

```
❌ Forgetting the comma in single-element tuples
   (5)    → int (not a tuple!)
   (5,)   → tuple

❌ Trying to modify a tuple
   t = (1, 2, 3)
   t[0] = 5  → TypeError (tuples are immutable)

❌ Confusing when to use tuples
   data = [1, 2, 3]  ← Changing data (use list)
   coords = (x, y)   ← Fixed data (use tuple)

❌ Modifying mutable items inside a tuple
   t = ([1, 2], [3, 4])
   t[0].append(3)  ← Works! (The list changed, not the tuple)
```

---

## 💻 Code Examples

### 📌 Example 1 — Creating Tuples

```python
# Basic tuples
point = (3, 4)
colors = ("red", "green", "blue")
mixed = (1, "hello", 3.14)

print(point)    # (3, 4)
print(colors)   # ("red", "green", "blue")
```

### 📌 Example 2 — Accessing Items

```python
record = ("Alice", 25, "Engineer")

print(record[0])  # Alice
print(record[-1]) # Engineer
print(record[1:]) # (25, "Engineer")
```

### 📌 Example 3 — Tuple Unpacking

```python
# Unpack coordinates
point = (10, 20)
x, y = point
print(f"X: {x}, Y: {y}")

# Unpack record
name, age, job = ("Bob", 30, "Developer")
print(f"{name} is {age}, works as {job}")
```

### 📌 Example 4 — Swapping Values

```python
a = 10
b = 20

# Traditional way (needs temp variable)
temp = a
a = b
b = temp

# Pythonic way (tuple unpacking)
a, b = b, a
print(f"a: {a}, b: {b}")  # a: 20, b: 10
```

### 📌 Example 5 — Tuples as Dictionary Keys

```python
# Tuples can be keys, lists cannot
locations = {
    (40, 74): "New York",
    (51, 0): "London",
    (35, 139): "Tokyo"
}

print(locations[(40, 74)])  # New York
```

### 📌 Example 6 — Returning Multiple Values

```python
def get_name_age():
    return "Alice", 25  # Returns a tuple!

name, age = get_name_age()
print(f"{name} is {age}")  # Alice is 25
```

---

## 🧪 Practice Exercise

1. Create a tuple with your name, age, and city
2. Unpack the tuple into three variables
3. Try to modify the tuple and see the error
4. Use a tuple as a dictionary key

---

## 📋 Key Takeaways

| Concept | Takeaway |
|---------|----------|
| 🔒 **Immutable** | Tuples cannot be changed after creation |
| ⚡ **Faster** | Python optimizes tuples for speed |
| 🔑 **Unpacking** | `x, y = point` assigns values cleanly |
| 🔄 **Swapping** | `a, b = b, a` swaps without temp variables |
| 📦 **Use case** | Fixed data, dictionary keys, multiple returns |

---

## 🔗 Further Reading

- 📖 [Tuples — Official Docs](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)
- 🔧 [Tuple Unpacking — Real Python](https://realpython.com/python-tuple-unpacking/)
- ⚡ [Lists vs Tuples — docs](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)