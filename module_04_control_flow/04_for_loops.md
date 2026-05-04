# 🔄 For Loops: Iterating Over Sequences

<p align="center">
  <img src="https://img.shields.io/badge/for-Iterate-blue?style=flat-square" alt="for">
  <img src="https://img.shields.io/badge/range()-Numbers-green?style=flat-square" alt="range">
  <img src="https://img.shields.io/badge/enumerate()-Index%20%2B%20Value-orange?style=flat-square" alt="enumerate">
</p>

> ### 💡 A `for` loop walks through a sequence one item at a time. Like reading a book — page by page, automatically.
> Learn how to loop over lists, strings, ranges, and more.

---

## 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- ✅ Use `for` loops to iterate over sequences
- ✅ Use `range()` to loop a specific number of times
- ✅ Use `enumerate()` and `zip()` for advanced iteration

---

## 🧠 Mental Model: A Conveyor Belt

A `for` loop is like a **conveyor belt** in a factory:

```
Items:  [🍎] → [🍌] → [🍊] → [🍇]
Loop:   Pick each item → Do something → Next item
```

You don't need to track positions — Python handles it for you.

---

## 📖 Basic Syntax

```python
for item in sequence:
    # Do something with item
```

### Key Rules

1. **`item`** is a variable — gets each value in the sequence
2. **`sequence`** can be a list, string, range, dict, etc.
3. **No manual indexing needed** — Python does it automatically

---

## 📊 What You Can Loop Over

| Type | Example | What `item` gets |
|------|---------|------------------|
| List | `for x in [1, 2, 3]` | Each number |
| String | `for c in "hi"` | Each character |
| Range | `for i in range(5)` | 0, 1, 2, 3, 4 |
| Dict | `for k in {"a": 1}` | Each key |
| Tuple | `for x in (1, 2)` | Each value |

---

## ⚠️ Common Mistakes

```
❌ Modifying a list while looping over it
   for item in my_list:
       my_list.remove(item)  → Dangerous! Can skip items

❌ Forgetting to use range() for counting
   for i in 5:       → TypeError
   for i in range(5): ← Correct

❌ Using range when you don't need indices
   for i in range(len(items)):     ← Verbose
       print(items[i])
   for item in items:              ← Cleaner
       print(item)

❌ Assuming for loop modifies original items
   for x in numbers:
       x += 1   → Does NOT change the list!
   Use indices or list comprehension instead
```

---

## 💻 Code Examples

### 📌 Example 1 — Loop Over a List

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(f"I like {fruit}")
```

### 📌 Example 2 — Loop Over a String

```python
word = "Python"

for char in word:
    print(char)
# P
# y
# t
# h
# o
# n
```

### 📌 Example 3 — Using `range()`

```python
# range(stop) — 0 to stop-1
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# range(start, stop)
for i in range(2, 6):
    print(i)  # 2, 3, 4, 5

# range(start, stop, step)
for i in range(0, 10, 2):
    print(i)  # 0, 2, 4, 6, 8
```

### 📌 Example 4 — `enumerate()` — Index + Value

```python
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
# 0: apple
# 1: banana
# 2: cherry
```

### 📌 Example 5 — `zip()` — Loop Over Two Lists

```python
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

for name, age in zip(names, ages):
    print(f"{name} is {age} years old")
```

### 📌 Example 6 — Nested For Loops

```python
# Multiplication table
for row in range(1, 4):
    for col in range(1, 4):
        print(f"{row} x {col} = {row * col}", end="\t")
    print()  # New line after each row
```

---

## 🧪 Practice Exercise

1. Loop over a list of your favorite foods and print each
2. Use `range()` to print numbers from 10 down to 1
3. Use `enumerate()` to print a numbered list
4. Use `zip()` to combine two lists into pairs

---

## 📋 Key Takeaways

| Concept | Takeaway |
|---------|----------|
| 🔄 **`for item in seq`** | Iterates over each item automatically |
| 🔢 **`range(n)`** | Generates numbers 0 to n-1 |
| 🔢 **`range(a, b, s)`** | Start, stop (exclusive), step |
| 🔢 **`enumerate()`** | Gives (index, value) pairs |
| 🔗 **`zip()`** | Pairs items from multiple sequences |

---

## 🔗 Further Reading

- 📖 [For Statements — Official Docs](https://docs.python.org/3/reference/compound_stmts.html#the-for-statement)
- 🔢 [Range Function — docs](https://docs.python.org/3/library/functions.html#func-range)
- 🌟 [Looping Techniques — docs](https://docs.python.org/3/tutorial/datastructures.html#looping-techniques)