# ➕ Arithmetic Operators: Math in Python

<p align="center">
  <img src="https://img.shields.io/badge/%2B-Add-blue?style=flat-square" alt="Add">
  <img src="https://img.shields.io/badge/%2A-Multiply-green?style=flat-square" alt="Multiply">
  <img src="https://img.shields.io/badge/%2F%2F-Floor%20Div-orange?style=flat-square" alt="Floor Div">
</p>

> ### 💡 Python is a calculator on steroids. It handles math the way you expect — plus some extra tricks you didn't know you needed.
> Learn all the ways Python can crunch numbers.

---

## 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- ✅ Use all arithmetic operators: `+`, `-`, `*`, `/`, `//`, `%`, `**`
- ✅ Understand the difference between `/` and `//`
- ✅ Use augmented assignment (`+=`, `-=`, etc.) to write cleaner code

---

## 🧠 Mental Model: A Scientific Calculator

Python is like a calculator. But instead of just `+`, `-`, `×`, `÷`, it has extra buttons:

```
Standard:  +  -  *  /
Python:    +  -  *  /  //  %  **
```

---

## 📖 The Operators

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| `+` | Addition | `10 + 3` | `13` |
| `-` | Subtraction | `10 - 3` | `7` |
| `*` | Multiplication | `10 * 3` | `30` |
| `/` | Division | `10 / 3` | `3.333...` |
| `//` | Floor Division | `10 // 3` | `3` |
| `%` | Modulus | `10 % 3` | `1` |
| `**` | Exponent | `10 ** 3` | `1000` |

---

## 🤔 `/` vs `//`: What's the Difference?

```
10 / 3   →  3.333333  (exact division — always returns float)
10 // 3  →  3         (floor division — rounds down to integer)
```

Think of `/` as "how much" and `//` as "how many whole times".

---

## 📊 The Modulus `%` Operator

The `%` gives you the **remainder** after division:

```
10 / 3 = 3 remainder 1
10 % 3 → 1
```

### 💡 What It's Used For

| Use Case | Code | Result |
|----------|------|--------|
| Is a number even? | `x % 2 == 0` | True/False |
| Is it divisible by 5? | `x % 5 == 0` | True/False |
| Wrap around (clock math) | `(hour + 1) % 24` | 0-23 |
| Group every N items | `i % 3 == 0` | Every 3rd item |

---

## ⚙️ Augmented Assignment (Shortcut)

Instead of `x = x + 5`, use `x += 5`:

| Long Form | Shortcut | Same As |
|-----------|----------|---------|
| `x = x + 5` | `x += 5` | Add 5 |
| `x = x - 3` | `x -= 3` | Subtract 3 |
| `x = x * 2` | `x *= 2` | Multiply by 2 |
| `x = x / 4` | `x /= 4` | Divide by 4 |

---

## ⚠️ Common Mistakes

```
❌ Mixing types in division
   10 / 2   → 5.0 (float, not 5!)
   10 // 2  → 5   (int, use this if you want a whole number)

❌ Confusing / and //
   7 / 2    → 3.5  (exact division)
   7 // 2   → 3    (floor division — rounds down)

❌ Modulus with floats
   10.5 % 3 → 1.5  (works, but often unexpected)

❌ Division by zero
   10 / 0   → ZeroDivisionError
   10 // 0  → ZeroDivisionError
   10 % 0   → ZeroDivisionError
```

---

## 💻 Code Examples

### 📌 Example 1 — Basic Arithmetic

```python
a = 10
b = 3

print(f"{a} + {b} = {a + b}")   # 13
print(f"{a} - {b} = {a - b}")   # 7
print(f"{a} * {b} = {a * b}")   # 30
print(f"{a} / {b} = {a / b}")   # 3.333...
```

### 📌 Example 2 — Floor Division vs True Division

```python
# True division — always returns float
print(10 / 3)    # 3.3333333333333335
print(10 / 2)    # 5.0 (still a float!)

# Floor division — rounds down, returns int
print(10 // 3)   # 3
print(10 // 2)   # 5
```

### 📌 Example 3 — Modulus in Action

```python
# Check if a number is even
x = 10
print(f"{x} is even: {x % 2 == 0}")  # True

# Check divisibility
y = 25
print(f"{y} divisible by 5: {y % 5 == 0}")  # True

# Wrap around (like a clock)
hour = 23
next_hour = (hour + 1) % 24
print(f"Next hour: {next_hour}")  # 0 (midnight)
```

### 📌 Example 4 — Exponentiation

```python
# Power
print(2 ** 10)     # 1024 (2^10)
print(5 ** 3)      # 125 (5^3)

# Square root (using 0.5)
print(16 ** 0.5)   # 4.0
print(27 ** (1/3)) # 3.0 (cube root)
```

### 📌 Example 5 — Order of Operations (PEMDAS)

```python
# Python follows PEMDAS:
# Parentheses → Exponents → Multiplication/Division → Addition/Subtraction

result = 2 + 3 * 4       # 14 (multiply first)
result = (2 + 3) * 4     # 20 (parentheses first)
result = 2 ** 3 * 4      # 32 (exponent first, then multiply)
result = 2 ** (3 * 4)    # 16777216 (parentheses first)

print(f"2 + 3 * 4 = {result}")
```

### 📌 Example 6 — Augmented Assignment

```python
score = 100

# Instead of: score = score + 10
score += 10
print(f"Score: {score}")  # 110

# Instead of: score = score - 5
score -= 5
print(f"Score: {score}")  # 105

# Instead of: score = score * 2
score *= 2
print(f"Score: {score}")  # 210
```

---

## 🧪 Practice Exercise

1. Calculate the area of a rectangle (length = 12, width = 5)
2. Find the remainder when 47 is divided by 7
3. Use exponentiation to calculate 2^8
4. Use augmented assignment to increment a counter from 0 to 10

---

## 📋 Key Takeaways

| Operator | Key Insight |
|----------|-------------|
| `/` | Always returns a float (e.g., `10/2 → 5.0`) |
| `//` | Floor division — rounds down (e.g., `10//3 → 3`) |
| `%` | Gives the remainder — great for even/odd checks |
| `**` | Exponent — `2**10` is 1024 |
| `+=` | Shortcut for `x = x + 5` — cleaner code |

---

## 🔗 Further Reading

- 📖 [Numeric Types — Official Docs](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)
- 🧮 [Python Arithmetic Operators — Real Python](https://realpython.com/python-operators-expressions/)
- 🔢 [Operator Precedence — docs](https://docs.python.org/3/reference/expressions.html#operator-precedence)