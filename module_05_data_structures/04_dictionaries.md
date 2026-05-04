# 📚 Dictionaries: Key-Value Lookups

<p align="center">
  <img src="https://img.shields.io/badge/dict-Key%20Value%20Pairs-blue?style=flat-square" alt="dict">
  <img src="https://img.shields.io/badge/Lookup-Fast%20O(1)-green?style=flat-square" alt="O(1)">
  <img src="https://img.shields.io/badge/Flexible-Any%20Data-orange?style=flat-square" alt="Flexible">
</p>

> ### 💡 A dictionary is like a real dictionary — you look up a word (key) to get its definition (value). No searching, just instant lookup.
> Learn how to store and retrieve data using keys.

---

## 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- ✅ Create and access dictionaries
- ✅ Add, modify, and remove key-value pairs
- ✅ Iterate over keys, values, and items
- ✅ Use common dict methods: `get`, `keys`, `values`, `items`

---

## 🧠 Mental Model: A Phone Book

A dictionary stores **key-value pairs**. Think of it like a phone book:

```
🔑 Key (Name)   →  📝 Value (Number)
"Alice"         →  "555-0123"
"Bob"           →  "555-0456"
```

You look up by name, not by position. Instant access!

---

## 📖 Creating Dictionaries

```python
# Empty dictionary
empty = {}

# Basic dictionary
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# Using dict() constructor
person = dict(name="Alice", age=25)
```

---

## 🔍 Accessing Values

```python
person = {"name": "Alice", "age": 25}

# Using brackets (crashes if missing)
print(person["name"])   # Alice

# Using get() (safe, returns None or default)
print(person.get("age"))       # 25
print(person.get("phone"))     # None
print(person.get("phone", "N/A"))  # "N/A"
```

---

## 📝 Modifying Dictionaries

```python
person = {"name": "Alice"}

# Add new key
person["age"] = 25

# Update existing
person["age"] = 26

# Remove
del person["age"]
phone = person.pop("phone", "N/A")
```

---

## ⚙️ Iterating Over Dictionaries

```python
data = {"a": 1, "b": 2, "c": 3}

for key in data:
    print(key)           # a, b, c

for value in data.values():
    print(value)         # 1, 2, 3

for key, value in data.items():
    print(f"{key}: {value}")  # a: 1, b: 2, c: 3
```

---

## ⚠️ Common Mistakes

```
❌ Accessing missing keys
   d = {"a": 1}
   d["b"]   → KeyError
   d.get("b")  ← Safe, returns None

❌ Using mutable keys
   d = {[1, 2]: "value"}  → TypeError (lists can't be keys)
   Use tuples instead: {(1, 2): "value"}

❌ Assuming order (Python 3.7+ preserves insertion order)
   d = {"b": 2, "a": 1}
   for k in d:  → b, a (order preserved in modern Python)

❌ Modifying while iterating
   for key in d:
       del d[key]  → RuntimeError
   Use list(d.keys()) if you must modify
```

---

## 💻 Code Examples

### 📌 Example 1 — Basic Dictionary

```python
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

print(person["name"])   # Alice
print(person.get("age"))  # 25
```

### 📌 Example 2 — Adding and Removing

```python
student = {"name": "Bob"}

student["age"] = 20
student["grade"] = "A"
print(student)  # {"name": "Bob", "age": 20, "grade": "A"}

del student["grade"]
print(student)  # {"name": "Bob", "age": 20}
```

### 📌 Example 3 — Iterating

```python
scores = {"Math": 95, "Science": 88, "History": 92}

for subject, score in scores.items():
    print(f"{subject}: {score}")
```

### 📌 Example 4 — Merging Dictionaries

```python
defaults = {"theme": "dark", "font": "12px"}
user_prefs = {"theme": "light", "language": "en"}

# Python 3.9+ merge operator
merged = defaults | user_prefs
print(merged)  # {"theme": "light", "font": "12px", "language": "en"}

# Older Python
merged = {**defaults, **user_prefs}
```

### 📌 Example 5 — Dictionary from Lists

```python
keys = ["name", "age", "city"]
values = ["Alice", 25, "NY"]

person = dict(zip(keys, values))
print(person)  # {"name": "Alice", "age": 25, "city": "NY"}
```

### 📌 Example 6 — Nested Dictionaries

```python
company = {
    "Alice": {"role": "Engineer", "salary": 80000},
    "Bob": {"role": "Designer", "salary": 75000}
}

print(company["Alice"]["role"])  # Engineer
```

---

## 🧪 Practice Exercise

1. Create a dictionary with 3 of your friends' names and ages
2. Add a new friend
3. Print all names using a loop
4. Use `get()` to safely access a missing key

---

## 📋 Key Takeaways

| Concept | Takeaway |
|---------|----------|
| 🔑 **Keys** | Must be unique and immutable (str, int, tuple) |
| 📝 **Values** | Can be any type, including lists or dicts |
| ⚡ **Lookup** | Instant access — `d["key"]` is O(1) |
| 🔍 **`get()`** | Safe access — returns None instead of crashing |
| 🔄 **`items()`** | Best way to loop over keys and values together |

---

## 🔗 Further Reading

- 📖 [Dictionaries — Official Docs](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
- 🌟 [Dictionary Methods — docs](https://docs.python.org/3/library/stdtypes.html#dict)
- 🔧 [Dict Comprehensions — docs](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)