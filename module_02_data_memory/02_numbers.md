# 🔢 The Primitive Types: Numbers (Int, Float, Complex)

<p align="center">
  <img src="https://img.shields.io/badge/int-Whole%20Numbers-blue?style=flat-square" alt="int">
  <img src="https://img.shields.io/badge/float-Decimal%20Numbers-green?style=flat-square" alt="float">
  <img src="https://img.shields.io/badge/complex-Real%20+%20Imaginary-purple?style=flat-square" alt="complex">
</p>

> ### 💡 Integers are like counting fingers — exact. Floats are like a measuring tape — approximate.
> Learn Python's three numeric types and why 0.1 + 0.2 doesn't equal 0.3.

---

## 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- ✅ Identify and use Python's three numeric types: int, float, and complex
- ✅ Perform arithmetic operations on each type
- ✅ Understand floating-point precision issues and when to avoid floats for money

---

## 🧠 Mental Model: Measuring Tape vs. Counting Fingers

| Type | Analogy | Description |
|------|---------|-------------|
| 🔢 **Integers** | Counting fingers | Whole, exact numbers |
| 📏 **Floats** | Measuring tape | Continuous, but with rounding |
| 🎯 **Complex** | 2D coordinate system | Real part + imaginary part |

---

## 📖 The Three Numeric Types

### 🔢 Integer (`int`) — Whole Numbers

Integers are exact, whole numbers with no decimal point.

| Example | Valid? |
|---------|-------|
| `42` | ✅ |
| `-10` | ✅ |
| `0` | ✅ |
| `1_000_000` | ✅ (underscores for readability) |
| `3.14` | ❌ (that's a float) |

### 📏 Float (`float`) — Decimal Numbers

Floats represent numbers with a decimal point. They can approximate most real numbers.

| Example | Valid? |
|---------|-------|
| `3.14` | ✅ |
| `-0.5` | ✅ |
| `100.0` | ✅ |
| `1e6` | ✅ (scientific notation: 1,000,000) |

### 🎯 Complex (`complex`) — Real + Imaginary

Complex numbers have a real part and an imaginary part (marked with `j`).

| Example | Real | Imaginary |
|---------|------|-----------|
| `3 + 4j` | 3.0 | 4.0 |
| `1 - 2j` | 1.0 | -2.0 |
| `5j` | 0.0 | 5.0 |

---

## ⚠️ The Floating-Point Gotcha

This is the **#1 surprise** for new Python developers:

```python
price = 0.1 + 0.2
print(price)  # 0.30000000000000004  ← NOT 0.3!
```

> 🚨 **Why?** Floats are stored in binary (base-2), and some decimal numbers can't be represented exactly in binary.

```python
# ✅ Solution for money: Use integers (cents)
price_cents = 10 + 20
print(price_cents)  # 30 cents — exact!

# Or use the decimal module for currency (later course)
```

---

## ⚠️ Common Mistakes

```
❌ Expecting float math to be exact
   0.1 + 0.2 == 0.3  → False (it's 0.30000000000000004)

❌ Using / when you want whole number division
   10 / 3  → 3.333... (float)
   Use // for floor division: 10 // 3  → 3

❌ Forgetting that int() truncates, not rounds
   int(3.9)  → 3 (not 4!)

❌ Using complex for everyday math
   c = 3 + 4j  ← Only use complex if you actually need it
```

---

## 💻 Code Examples

### 📌 Example 1 — Integer Operations

```python
# All basic math with integers
a = 10
b = 3

print(a + b)     # 13 (addition)
print(a - b)     # 7  (subtraction)
print(a * b)     # 30 (multiplication)
print(a / b)     # 3.333... (division → always float!)
print(a // b)    # 3  (floor division → rounds down)
print(a % b)     # 1  (modulus → remainder)
print(a ** b)    # 1000 (exponent → 10^3)
```

### 📌 Example 2 — Float Operations

```python
# Floats work the same way
x = 10.5
y = 2.0

print(x + y)     # 12.5
print(x * y)     # 21.0
print(x / y)     # 5.25
```

### 📌 Example 3 — Mixed int and float

```python
# When int and float mix, the result is always float
i = 10     # int
f = 2.5    # float

print(i + f)    # 12.5 (float)
print(i * f)    # 25.0 (float)
```

### 📌 Example 4 — Complex Numbers

```python
# Complex numbers have real and imaginary parts
c1 = 3 + 4j
c2 = 1 + 2j

print(c1 + c2)     # (4+6j)
print(c1 * c2)     # (-5+10j)

# Access parts
c = 3 + 4j
print(c.real)      # 3.0
print(c.imag)      # 4.0
```

### 📌 Example 5 — Checking Types

```python
# Every number has a type
x = 42
y = 3.14
z = 3 + 4j

print(type(x))     # <class 'int'>
print(type(y))     # <class 'float'>
print(type(z))     # <class 'complex'>
```

---

## 🧪 Practice Exercise

1. Create an integer variable for your age
2. Create a float variable for your height in meters
3. Calculate your age in 10 years
4. Print both using an f-string

**Bonus:** Create a complex number and print its real and imaginary parts.

---

## 📋 Key Takeaways

| Concept | Takeaway |
|---------|----------|
| 🔢 **`int`** | Whole numbers (`42`, `-10`, `0`) — exact |
| 📏 **`float`** | Decimal numbers (`3.14`, `-0.5`) — approximations |
| 🎯 **`complex`** | Real + imaginary (`3 + 4j`) — for advanced math |
| ⚠️ **Float math can be imprecise** | Use integers for money |
| ➗ **Division (`/`) always returns float** | Use `//` for whole numbers |

---

## 🔗 Further Reading

- 📖 [Python Numeric Types — Official Docs](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)
- 🔬 [Floating-Point Arithmetic — Python Docs](https://docs.python.org/3/tutorial/floatingpoint.html) — Why 0.1 + 0.2 != 0.3
- 💰 [Python's decimal Module](https://docs.python.org/3/library/decimal.html) — For precise decimal arithmetic