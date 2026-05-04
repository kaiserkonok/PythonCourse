# 🔄 Type Casting: Converting Data Between Types

<p align="center">
  <img src="https://img.shields.io/badge/int()-Integer-blue?style=flat-square" alt="int()">
  <img src="https://img.shields.io/badge/float()-Float-green?style=flat-square" alt="float()">
  <img src="https://img.shields.io/badge/str()-String-orange?style=flat-square" alt="str()">
</p>

> ### 💡 Type casting is like a currency exchange — you have dollars, you want euros. Python converts one to the other.
> Learn how to convert between strings, integers, and floats.

---

## 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- ✅ Convert between strings, integers, and floats using `int()`, `float()`, and `str()`
- ✅ Handle conversion errors with `try/except`
- ✅ Know when and why type conversion is necessary

---

## 🧠 Mental Model: Currency Exchange

Type casting is like **exchanging currency**.

| You Have | You Want | Python Does |
|----------|----------|-------------|
| 💵 `"42"` (string) | 🔢 `42` (integer) | `int("42")` |
| 🔢 `42` (integer) | 📝 `"42"` (string) | `str(42)` |
| 📝 `"3.14"` (string) | 📏 `3.14` (float) | `float("3.14")` |

---

## 📖 The Conversion Functions

| Function | Converts To | Example |
|----------|-------------|----------|
| `int()` | Integer | `int("42")` → `42` |
| `float()` | Float | `float("3.14")` → `3.14` |
| `str()` | String | `str(42)` → `"42"` |
| `bool()` | Boolean | `bool(1)` → `True` |

---

## 🤔 Why Convert?

Most often, you need to convert when:

1. 👤 **Getting user input** — `input()` always returns a string
2. 📝 **Combining text and numbers** — you can't add strings and ints
3. 📁 **Reading from files** — data comes in as strings
4. 🌐 **API responses** — JSON numbers are often strings

```python
# Example: User input
age = input("Enter your age: ")  # Returns "25" (string)
age = int(age)                   # Now it's 25 (integer)
print(f"Next year you'll be {age + 1}")
```

---

## 📊 The Rules

### 🔢 int() — Converts to Integer

| Input | Result | Why |
|-------|--------|-----|
| `int("42")` | `42` | ✅ Valid integer string |
| `int(3.14)` | `3` | ⚠️ **Truncates** (not rounds) |
| `int("3.14")` | **Error** | ❌ Can't convert decimal string directly |
| `int("hello")` | **Error** | ❌ Not a number |

### 📏 float() — Converts to Float

| Input | Result | Why |
|-------|--------|-----|
| `float("3.14")` | `3.14` | ✅ Valid float string |
| `float(42)` | `42.0` | ✅ Int becomes float |
| `float("42")` | `42.0` | ✅ Integer string becomes float |

### 📝 str() — Converts to String

| Input | Result |
|-------|--------|
| `str(42)` | `"42"` |
| `str(3.14)` | `"3.14"` |
| `str(True)` | `"True"` |
| `str([1, 2, 3])` | `"[1, 2, 3]"` |

---

## ⚠️ Common Mistakes

```
❌ Forgetting that int() truncates, not rounds
   int(3.9)  → 3 (not 4!)
   Use round() if you want rounding: round(3.9)  → 4

❌ Trying to convert a decimal string directly to int
   int("3.14")  → ValueError
   Use float first: int(float("3.14"))  → 3

❌ Not handling invalid conversions
   int("hello")  → ValueError (crashes!)
   Use try/except to handle it gracefully
```

---

## 💻 Code Examples

### 📌 Example 1 — String to Integer

```python
# Convert a string number to integer
num_str = "42"
num_int = int(num_str)

print(num_int)        # 42
print(type(num_int))  # <class 'int'>
```

### 📌 Example 2 — Integer to String

```python
# Convert a number to string (for display or concatenation)
age = 25
age_str = str(age)

print(age_str)        # "25"
print(type(age_str))  # <class 'str'>
```

### 📌 Example 3 — String to Float

```python
price = float("19.99")
print(price)          # 19.99
print(type(price))    # <class 'float'>
```

### 📌 Example 4 — Chained Conversions

```python
# String → Int → Float
value = "42"
result = float(int(value))

print(result)         # 42.0
print(type(result))   # <class 'float'>
```

### 📌 Example 5 — Handling Conversion Errors

```python
# Invalid conversion will crash your program without try/except
try:
    result = int("hello")
except ValueError:
    print("Cannot convert 'hello' to integer!")

# Safe conversion function
def safe_int(value):
    try:
        return int(value)
    except ValueError:
        return None

print(safe_int("42"))   # 42
print(safe_int("hello"))  # None
```

### 📌 Example 6 — Base Conversions

```python
# int() can convert from different number bases
binary = int("1010", 2)    # Binary to decimal
hex_num = int("FF", 16)    # Hexadecimal to decimal
octal = int("77", 8)       # Octal to decimal

print(f"Binary 1010 = {binary}")   # 10
print(f"Hex FF = {hex_num}")       # 255
print(f"Octal 77 = {octal}")       # 63
```

---

## 🧪 Practice Exercise

1. Convert string `"100"` to integer and multiply by 2
2. Convert integer `50` to string and concatenate with `" dollars"`
3. Try converting `"hello"` to integer and handle the error
4. Convert float `3.14159` to integer

---

## 📋 Key Takeaways

| Concept | Takeaway |
|---------|----------|
| 🔢 **`int()`** | Converts to integer — truncates floats, crashes on invalid strings |
| 📏 **`float()`** | Converts to float — handles integer strings too |
| 📝 **`str()`** | Converts anything to string — always safe |
| ⚠️ **`int("3.14")` fails** | Use `int(float("3.14"))` instead |
| 🛡️ **`try/except`** | Handles conversion errors gracefully |

---

## 🔗 Further Reading

- 📖 [Python Built-in Functions — docs](https://docs.python.org/3/library/functions.html) — `int()`, `float()`, `str()` reference
- 🛡️ [Exception Handling — Official Docs](https://docs.python.org/3/tutorial/errors.html)
- 🔢 [Number Bases in Python](https://docs.python.org/3/library/functions.html#int) — Binary, hex, octal conversions