# 📥 Parameters & Arguments: Flexible Function Inputs

<p align="center">
  <img src="https://img.shields.io/badge/args-Positional-blue?style=flat-square" alt="args">
  <img src="https://img.shields.io/badge/kwargs-Keyword-green?style=flat-square" alt="kwargs">
  <img src="https://img.shields.io/badge/defaults-Flexible-orange?style=flat-square" alt="defaults">
</p>

> ### 💡 Parameters and arguments are how your function gets its ingredients. Learn all the ways to pass data — from simple values to flexible collections.
> Master positional, keyword, default, and *args/**kwargs.

---

## 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- ✅ Use positional and keyword arguments
- ✅ Set default parameter values
- ✅ Use `*args` and `**kwargs` for flexible inputs
- ✅ Understand the correct order of parameters

---

## 🧠 Mental Model: Ordering Food

Arguments are like **ordering food** — you can specify items by position or by name:

```
🍔 Burger + 🍟 Fries  ← Positional (order matters)
🥤 Drink=Coke        ← Keyword (name=value)
🍟 Extra=Fries       ← Optional (uses default if not given)
```

---

## 📖 Types of Arguments

| Type | Syntax | Example |
|------|--------|---------|
| Positional | `func(a, b)` | `func(1, 2)` |
| Keyword | `func(key=value)` | `func(a=1, b=2)` |
| Default | `def func(a=1)` | `func()` uses 1 |
| `*args` | `def func(*args)` | `func(1, 2, 3)` |
| `**kwargs` | `def func(**kwargs)` | `func(a=1, b=2)` |

---

## 📊 The Parameter Order

Python requires parameters in this order:

```python
def func(positional, *args, keyword=value, **kwargs):
    pass
```

1. **Positional** (required)
2. **`*args`** (extra positional)
3. **Keyword** (with defaults)
4. **`**kwargs`** (extra keyword)

---

## ⚠️ Common Mistakes

```
❌ Mutable defaults
   def add_item(item, lst=[]):  ← Dangerous!
       lst.append(item)
       return lst
   # Default list is shared across all calls!

   def add_item(item, lst=None):  ← Safe
       if lst is None:
           lst = []
       lst.append(item)
       return lst

❌ Mixing positional and keyword incorrectly
   func(1, a=2)  ← If 'a' is first param, this is an error
   func(1, b=2)  ← OK if second param is 'b'

❌ Too many positional arguments
   def greet(name):
       pass
   greet("Alice", "Bob")  → TypeError

❌ Forgetting * and ** syntax
   def func(*args)    ← Collects extra positional
   def func(args)     ← Just one parameter
```

---

## 💻 Code Examples

### 📌 Example 1 — Positional Arguments

```python
def describe(name, age, city):
    print(f"{name} is {age}, lives in {city}")

describe("Alice", 25, "NY")  # Order matters!
```

### 📌 Example 2 — Keyword Arguments

```python
describe(age=25, city="NY", name="Alice")  # Order doesn't matter!
```

### 📌 Example 3 — Default Values

```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")           # Hello, Alice!
greet("Bob", "Hi")       # Hi, Bob!
```

### 📌 Example 4 — `*args` (Variable Positional)

```python
def total(*numbers):
    return sum(numbers)

print(total(1, 2, 3))      # 6
print(total(10, 20, 30, 40))  # 100
```

### 📌 Example 5 — `**kwargs` (Variable Keyword)

```python
def build_profile(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

build_profile(name="Alice", age=25, job="Dev")
```

### 📌 Example 6 — Combining All

```python
def full_example(a, b, *args, x=10, y=20, **kwargs):
    print(f"Positional: {a}, {b}")
    print(f"Extra: {args}")
    print(f"Keywords: {x}, {y}")
    print(f"Extra kwargs: {kwargs}")

full_example(1, 2, 3, 4, 5, x=100, y=200, z=300)
```

---

## 🧪 Practice Exercise

1. Create a function with default parameters
2. Write a function that takes `*args` and returns their product
3. Use `**kwargs` to create a flexible config function
4. Combine positional, `*args`, and `**kwargs`

---

## 📋 Key Takeaways

| Concept | Takeaway |
|---------|----------|
| 📍 **Positional** | Order matters — `func(a, b)` |
| 🔑 **Keyword** | Order doesn't matter — `func(a=1, b=2)` |
| 🛡️ **Defaults** | `def func(a=1)` — optional inputs |
| ⭐ **`*args`** | Collects extra positional arguments into a tuple |
| 🔹 **`**kwargs`** | Collects extra keyword arguments into a dict |

---

## 🔗 Further Reading

- 📖 [More on Defining Functions — Official Docs](https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions)
- 🌟 [*args and **kwargs — Real Python](https://realpython.com/python-kwargs-and-args/)
- 🔧 [Mutable Default Arguments — docs](https://docs.python.org/3/tutorial/controlflow.html#default-argument-values)