# 📦 Lists: Your Data Backpack

<p align="center">
  <img src="https://img.shields.io/badge/list-Ordered%20Collection-blue?style=flat-square" alt="list">
  <img src="https://img.shields.io/badge/Mutable-Changeable-green?style=flat-square" alt="mutable">
  <img src="https://img.shields.io/badge/Index-0%20based-orange?style=flat-square" alt="0-indexed">
</p>

> ### 💡 A list is like a backpack — you can throw things in, take them out, rearrange them, and find them by their position.
> Learn how to store and manage collections of data in Python.

---

## 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- ✅ Create, access, and modify lists
- ✅ Use common list methods: `append`, `remove`, `pop`, `sort`
- ✅ Understand the difference between copying and aliasing lists

---

## 🧠 Mental Model: A Backpack

A list is an **ordered collection** of items. Think of it like a backpack:

```
[📱 Phone] [💧 Water] [🥪 Sandwich] [🔑 Keys]
  0          1          2              3
```

You can:
- 📥 Add things to the end or middle
- 📤 Take things out
- 🔀 Rearrange them
- 🔍 Find things by position

---

## 📖 Creating Lists

```python
# Empty list
empty = []

# List of mixed types (yes, Python allows this!)
mixed = [1, "hello", 3.14, True]

# List of numbers
numbers = [10, 20, 30, 40, 50]
```

> 💡 Lists can hold **any type** of data, even other lists!

---

## 📍 Accessing Items

Just like strings, lists use **0-based indexing** and **slicing**:

```python
colors = ["red", "green", "blue", "yellow"]

print(colors[0])    # red (first)
print(colors[-1])   # yellow (last)
print(colors[1:3])  # ["green", "blue"]
```

---

## ⚙️ Modifying Lists

Lists are **mutable** — you can change them after creation:

```python
fruits = ["apple", "banana", "cherry"]

fruits[1] = "orange"        # Replace: ["apple", "orange", "cherry"]
fruits.append("grape")      # Add to end: [..., "grape"]
fruits.insert(1, "pear")    # Insert at index: ["apple", "pear", "orange", ...]
fruits.remove("cherry")     # Remove by value
popped = fruits.pop()       # Remove last item and return it
```

---

## 🔧 Useful List Methods

| Method | What it does | Example |
|--------|-------------|---------|
| `append(x)` | Adds `x` to end | `l.append(5)` |
| `insert(i, x)` | Inserts `x` at index `i` | `l.insert(0, 10)` |
| `remove(x)` | Removes first occurrence of `x` | `l.remove("hi")` |
| `pop()` | Removes and returns last item | `x = l.pop()` |
| `sort()` | Sorts in place | `l.sort()` |
| `reverse()` | Reverses in place | `l.reverse()` |
| `index(x)` | Finds position of `x` | `l.index("hi")` |
| `count(x)` | Counts occurrences of `x` | `l.count(5)` |

---

## ⚠️ Common Mistakes

```
❌ Out of bounds indexing
   colors = ["red", "blue"]
   colors[2]  → IndexError (only indices 0 and 1 exist)

❌ Modifying while iterating
   for x in my_list:
       my_list.remove(x)  → Skips items or crashes!

❌ Confusing append vs extend
   [1, 2].append([3, 4])  → [1, 2, [3, 4]] (nested list)
   [1, 2].extend([3, 4])  → [1, 2, 3, 4] (flattened)

❌ Aliasing vs Copying
   a = [1, 2, 3]
   b = a          ← Alias (both point to same list)
   b = a.copy()   ← Copy (independent list)
   b[0] = 99
   print(a)       ← Changes in b affect a if aliased!
```

---

## 💻 Code Examples

### 📌 Example 1 — Basic List Operations

```python
numbers = [10, 20, 30]

# Access
print(numbers[0])  # 10

# Modify
numbers[1] = 25
print(numbers)     # [10, 25, 30]

# Add
numbers.append(40)
print(numbers)     # [10, 25, 30, 40]
```

### 📌 Example 2 — Insert and Remove

```python
fruits = ["apple", "cherry"]

fruits.insert(1, "banana")
print(fruits)  # ["apple", "banana", "cherry"]

fruits.remove("cherry")
print(fruits)  # ["apple", "banana"]

last = fruits.pop()
print(f"Popped: {last}, List: {fruits}")
```

### 📌 Example 3 — Sorting and Reversing

```python
scores = [85, 92, 78, 90, 88]

scores.sort()
print(f"Ascending: {scores}")  # [78, 85, 88, 90, 92]

scores.reverse()
print(f"Descending: {scores}")  # [92, 90, 88, 85, 78]
```

### 📌 Example 4 — Slicing Lists

```python
letters = ['a', 'b', 'c', 'd', 'e']

print(letters[:3])    # ['a', 'b', 'c'] (first 3)
print(letters[2:])    # ['c', 'd', 'e'] (from index 2)
print(letters[::2])   # ['a', 'c', 'e'] (every 2nd)
print(letters[::-1])  # ['e', 'd', 'c', 'b', 'a'] (reverse)
```

### 📌 Example 5 — Checking Membership

```python
colors = ["red", "green", "blue"]

if "red" in colors:
    print("Found red!")

print(len(colors))    # 3 (length)
print(colors.count("green"))  # 1
```

### 📌 Example 6 — Copying Lists

```python
original = [1, 2, 3]

# Alias (dangerous)
alias = original
alias[0] = 99
print(original)  # [99, 2, 3] — changed!

# Safe copy
safe_copy = original.copy()
safe_copy[0] = 1
print(original)  # [99, 2, 3] — unchanged
```

---

## 🧪 Practice Exercise

1. Create a list of your 5 favorite movies
2. Add a new movie to the end
3. Remove the first movie
4. Sort the list alphabetically
5. Print the reversed list

---

## 📋 Key Takeaways

| Concept | Takeaway |
|---------|----------|
| 📦 **Lists are ordered** | Items keep their position (0, 1, 2...) |
| 📝 **Lists are mutable** | You can add, remove, and change items |
| 🔄 **Methods change in place** | `sort()`, `reverse()` modify the original list |
| 📋 **`append` vs `extend`** | `append` adds one item, `extend` adds many |
| ⚠️ **Copying matters** | Use `.copy()` or `[:]` to avoid aliasing bugs |

---

## 🔗 Further Reading

- 📖 [Lists — Official Docs](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
- 🛠️ [List Methods — docs](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
- 🌐 [Copying Lists — Real Python](https://realpython.com/copying-python-lists/)