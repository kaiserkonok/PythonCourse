# 🧠 Logical Operators: Combining Conditions

<p align="center">
  <img src="https://img.shields.io/badge/and-Both%20must%20be%20true-blue?style=flat-square" alt="and">
  <img src="https://img.shields.io/badge/or-At%20least%20one-green?style=flat-square" alt="or">
  <img src="https://img.shields.io/badge/not-Invert-orange?style=flat-square" alt="not">
</p>

> ### 💡 Logical operators let you combine multiple conditions. Like wiring multiple switches to control one light.
> Learn how to use `and`, `or`, and `not` to build complex logic.

---

## 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- ✅ Use `and`, `or`, and `not` to combine boolean conditions
- ✅ Understand short-circuit evaluation
- ✅ Write complex conditions that are still readable

---

## 🧠 Mental Model: Light Switches

Think of logical operators like **wiring light switches**:

| Operator | Wiring | Light turns ON when... |
|----------|--------|------------------------|
| `and` | Series (in a line) | **Both** switches are ON |
| `or` | Parallel (side by side) | **At least one** switch is ON |
| `not` | Reverse wiring | Light is ON when switch is OFF |

---

## 📖 The Operators

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `and` | Both must be True | `True and False` | `False` |
| `or` | At least one must be True | `True or False` | `True` |
| `not` | Inverts the value | `not True` | `False` |

### Truth Tables

```
A     B     A and B    A or B    not A
True  True  True       True      False
True  False False      True      False
False True  False      True      True
False False False      False     True
```

---

## 🤔 Real-World Examples

```python
# AND — both must be True
has_ticket = True
has_id = True
can_enter = has_ticket and has_id  # True

# OR — at least one must be True
is_weekend = True
is_holiday = False
can_sleep_in = is_weekend or is_holiday  # True

# NOT — inverts
is_raining = True
need_umbrella = not is_raining  # False
```

---

## ⚡ Short-Circuit Evaluation

Python is lazy — it stops checking as soon as it knows the answer:

```python
# AND: stops at first False
False and print("This won't run!")  # Stops at False

# OR: stops at first True
True or print("This won't run!")    # Stops at True
```

This is useful for safe checks:

```python
# Instead of:
if user is not None and user.is_active:
    ...

# Python checks `user is not None` first
# If False, it never checks `user.is_active` — no crash!
```

---

## ⚠️ Common Mistakes

```
❌ Using `and` when you mean `or`
   if temp > 100 and temp < 0:   → Always False (impossible!)
   if temp > 100 or temp < 0:    ← Correct (extreme temperatures)

❌ Chaining comparisons incorrectly
   if x == 1 or 2 or 3:          → Always True (non-zero is Truthy!)
   if x in (1, 2, 3):            ← Correct

❌ Overcomplicating conditions
   if (is_raining == True and has_umbrella == True):  ← Verbose
   if is_raining and has_umbrella:                    ← Clean

❌ Forgetting operator precedence
   True or True and False  → True (and first)
   (True or True) and False → False (parentheses change order)
```

---

## 💻 Code Examples

### 📌 Example 1 — Basic `and`

```python
is_adult = True
has_license = True

# Both must be True
can_drive = is_adult and has_license
print(f"Can drive: {can_drive}")  # True

# One is False
has_license = False
can_drive = is_adult and has_license
print(f"Can drive: {can_drive}")  # False
```

### 📌 Example 2 — Basic `or`

```python
is_weekend = False
is_holiday = True

# At least one must be True
can_sleep_in = is_weekend or is_holiday
print(f"Can sleep in: {can_sleep_in}")  # True

# Both False
is_holiday = False
can_sleep_in = is_weekend or is_holiday
print(f"Can sleep in: {can_sleep_in}")  # False
```

### 📌 Example 3 — Basic `not`

```python
is_raining = True

# Invert the value
print(f"It is raining: {is_raining}")        # True
print(f"It is NOT raining: {not is_raining}") # False
```

### 📌 Example 4 — Combining Multiple Operators

```python
age = 25
has_ticket = True
is_member = False

# VIP entry: must be adult AND (has ticket OR is member)
can_enter = age >= 18 and (has_ticket or is_member)
print(f"Can enter: {can_enter}")  # True
```

### 📌 Example 5 — Operator Precedence

```python
# Order: not > and > or (like PEMDAS for logic)

result = True or True and False
# Evaluates as: True or (True and False) → True or False → True

result = not False and True or False
# Evaluates as: (not False) and True or False → True and True or False → True

print(f"Result: {result}")
```

### 📌 Example 6 — Practical Use Cases

```python
# Check if a year is a leap year
year = 2024
is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
print(f"{year} is leap: {is_leap}")  # True

# Validate user input
username = "admin"
password = "secret123"
is_admin = True

login_success = (username == "admin" and password == "secret123") and is_admin
print(f"Login: {login_success}")
```

---

## 🧪 Practice Exercise

1. Create two boolean variables and combine them with `and`
2. Use `or` to check if a number is negative OR greater than 100
3. Use `not` to invert a boolean
4. Write a complex condition with parentheses to control order

---

## 📋 Key Takeaways

| Operator | Key Insight |
|----------|-------------|
| `and` | Both must be True — stops at first False |
| `or` | At least one must be True — stops at first True |
| `not` | Inverts the value — `not True → False` |
| 🔗 **Precedence** | `not` > `and` > `or` — use parentheses to be clear |
| ⚡ **Short-circuit** | Python stops early — useful for safe checks |

---

## 🔗 Further Reading

- 📖 [Boolean Operations — Official Docs](https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not)
- ⚡ [Short-Circuit Evaluation — docs](https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not)
- 🧮 [Operator Precedence — docs](https://docs.python.org/3/reference/expressions.html#operator-precedence)