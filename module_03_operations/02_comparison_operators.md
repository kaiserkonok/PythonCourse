# ⚖️ Comparison Operators: Asking Questions in Python

<p align="center">
  <img src="https://img.shields.io/badge/%3D%3D-Equal-blue?style=flat-square" alt="Equal">
  <img src="https://img.shields.io/badge/%21%3D-Not%20Equal-green?style=flat-square" alt="Not Equal">
  <img src="https://img.shields.io/badge/%3C%3E-Greater%20Less-orange?style=flat-square" alt="Greater Less">
</p>

> ### 💡 Comparison operators are the questions Python asks to make decisions. Every `if` statement starts here.
> Learn how to compare values and get `True` or `False` answers.

---

## 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- ✅ Use all comparison operators: `==`, `!=`, `>`, `<`, `>=`, `<=`
- ✅ Compare numbers, strings, and variables
- ✅ Understand the difference between `=` and `==`

---

## 🧠 Mental Model: The Question Mark

If arithmetic operators are statements (`10 + 3`), comparison operators are **questions**:

```
10 == 3?   → False (Is 10 equal to 3?)
10 > 3?    → True  (Is 10 greater than 3?)
10 <= 10?  → True  (Is 10 less than or equal to 10?)
```

Every comparison returns a **boolean** — `True` or `False`.

---

## 📖 The Operators

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `==` | Equal | `10 == 10` | `True` |
| `!=` | Not Equal | `10 != 5` | `True` |
| `>` | Greater Than | `10 > 5` | `True` |
| `<` | Less Than | `10 < 5` | `False` |
| `>=` | Greater or Equal | `10 >= 10` | `True` |
| `<=` | Less or Equal | `10 <= 5` | `False` |

---

## ⚠️ `=` vs `==`: The Classic Beginner Trap

```python
# =  → Assignment (gives a value)
# == → Comparison (asks a question)

x = 10       # Give x the value 10
x == 10      # Ask: is x equal to 10? → True
```

> 💡 Think of `=` as **putting** something in a box, and `==` as **checking** what's in the box.

---

## 📊 Comparing Different Types

### 🔢 Numbers

```python
print(10 > 5)       # True
print(10 == 10)     # True
print(3.14 <= 3.14) # True
print(5 != 5)       # False
```

### 📝 Strings

Strings are compared **alphabetically** (lexicographically):

```python
print("apple" < "banana")   # True (a comes before b)
print("Python" == "python") # False (case-sensitive!)
print("cat" != "dog")       # True
```

### 🌟 Chained Comparisons

Python lets you chain comparisons naturally:

```python
x = 15

# Traditional
x > 10 and x < 20   # True

# Pythonic (chained)
10 < x < 20         # True (same result, cleaner)
```

---

## ⚠️ Common Mistakes

```
❌ Using = instead of == in conditions
   if x = 5:        → SyntaxError
   if x == 5:       ← Correct

❌ Forgetting case sensitivity in strings
   "Python" == "python"  → False

 Comparing floats directly
   0.1 + 0.2 == 0.3  → False (floating-point precision!)
   Use rounding or tolerance instead

❌ Mixing types in comparisons
   5 == "5"   → False (int vs string — never equal!)
```

---

## 💻 Code Examples

### 📌 Example 1 — Basic Comparisons

```python
a = 10
b = 5

print(f"{a} > {b}: {a > b}")    # True
print(f"{a} < {b}: {a < b}")    # False
print(f"{a} == {b}: {a == b}")  # False
print(f"{a} != {b}: {a != b}")  # True
```

### 📌 Example 2 — Comparison with Variables

```python
age = 20
minimum_age = 18

can_vote = age >= minimum_age
print(f"Can vote: {can_vote}")  # True

score = 95
passing_score = 50

passed = score >= passing_score
print(f"Passed: {passed}")  # True
```

### 📌 Example 3 — String Comparisons

```python
name1 = "Alice"
name2 = "Bob"

print(f"{name1} < {name2}: {name1 < name2}")  # True (alphabetical)
print(f"{name1} == {name2}: {name1 == name2}")  # False

# Case sensitivity matters
print(f"'python' == 'Python': {'python' == 'Python'}")  # False

# Case-insensitive comparison
print(f"'python'.lower() == 'Python'.lower(): {'python'.lower() == 'Python'.lower()}")  # True
```

### 📌 Example 4 — Chained Comparisons

```python
x = 15

# Traditional way
print(x > 10 and x < 20)   # True

# Pythonic chained way
print(10 < x < 20)         # True

# Check if in range
print(0 <= x <= 100)       # True (percentage check)
```

### 📌 Example 5 — Comparing Different Types

```python
# Numbers vs Strings — never equal
print(5 == "5")     # False
print(5 != "5")     # True

# Booleans are special — True is 1, False is 0
print(True == 1)    # True
print(False == 0)   # True
print(True > 0)     # True
```

### 📌 Example 6 — The `is` vs `==` Gotcha

```python
# == checks if values are equal
# is checks if they are the exact same object in memory

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)   # True (same values)
print(a is b)   # False (different objects!)

# For simple values, Python optimizes and they may be the same
x = 10
y = 10
print(x == y)   # True
print(x is y)   # True (small integers are cached)
```

---

## 🧪 Practice Exercise

1. Compare two numbers: 25 and 18 — is the first greater?
2. Check if your name equals "Alice"
3. Use a chained comparison to check if a number is between 1 and 100
4. Compare two strings case-insensitively

---

## 📋 Key Takeaways

| Operator | Key Insight |
|----------|-------------|
| `==` | Asks "are they equal?" (not assignment!) |
| `!=` | Asks "are they different?" |
| `>=` / `<=` | Includes equality — `5 >= 5` is `True` |
| 🔗 **Chaining** | `10 < x < 20` is Pythonic and clean |
| 📝 **Strings** | Compared alphabetically and case-sensitive |

---

## 🔗 Further Reading

- 📖 [Comparison Operators — Official Docs](https://docs.python.org/3/reference/expressions.html#comparisons)
- 🌟 [Chained Comparisons — Python Docs](https://docs.python.org/3/reference/expressions.html#comparisons)
- 🔧 [`is` vs `==` — Real Python](https://realpython.com/python-is-operator/)