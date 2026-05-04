# 🔀 Conditional Branching: Making Decisions with `if`

<p align="center">
  <img src="https://img.shields.io/badge/if-Condition-blue?style=flat-square" alt="if">
  <img src="https://img.shields.io/badge/elif-Else%20If-green?style=flat-square" alt="elif">
  <img src="https://img.shields.io/badge/else-Fallback-orange?style=flat-square" alt="else">
</p>

> ### 💡 `if` statements are the crossroads of programming — they let your code choose different paths based on conditions.
> Learn how to make your programs react to different situations.

---

## 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- ✅ Use `if`, `elif`, and `else` to control code flow
- ✅ Write nested conditions for complex logic
- ✅ Use indentation correctly (Python's unique syntax)

---

## 🧠 Mental Model: A Fork in the Road

An `if` statement is like a **fork in the road**:

```
                    ┌──> Path A (if condition is True)
Start ── Condition ─┤
                    └──> Path B (else)
```

Python checks the condition and takes **one path** — never both.

---

## 📖 The Structure

```python
if condition:
    # Run if condition is True
elif another_condition:
    # Run if first was False but this is True
else:
    # Run if all above were False
```

### Key Rules

1. **`if`** is required — must come first
2. **`elif`** is optional — can have zero or many
3. **`else`** is optional — can have zero or one
4. **Indentation matters** — 4 spaces defines the block

---

## 📊 Examples at a Glance

| Pattern | Code |
|---------|------|
| Simple `if` | `if x > 0: print("positive")` |
| `if/else` | `if x > 0: ... else: ...` |
| `if/elif/else` | `if x > 0: ... elif x == 0: ... else: ...` |
| Nested | `if x > 0: if x > 10: ...` |

---

## ⚠️ Common Mistakes

```
❌ Forgetting the colon
   if x > 0        → SyntaxError
   if x > 0:       ← Correct

❌ Wrong indentation
   if x > 0:
   print("hi")     → IndentationError
       print("hi") ← Correct (4 spaces)

❌ Using = instead of ==
   if x = 5:       → SyntaxError
   if x == 5:      ← Correct

❌ Forgetting elif (using multiple ifs)
   if x > 0: ...
   if x == 0: ...  ← All checked (wasteful)
   elif x == 0: ... ← Only checked if first is False
```

---

## 💻 Code Examples

### 📌 Example 1 — Simple `if`

```python
age = 20

if age >= 18:
    print("You are an adult")
    print("You can vote")

print("This always runs")
```

### 📌 Example 2 — `if/else`

```python
temperature = 30

if temperature > 25:
    print("It's warm outside")
else:
    print("It's cold outside")
```

### 📌 Example 3 — `if/elif/else`

```python
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Grade: {grade}")  # B
```

### 📌 Example 4 — Nested Conditions

```python
age = 25
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("Bring ID")
else:
    print("Too young")
```

### 📌 Example 5 — Multiple Conditions

```python
age = 25
is_student = True

# AND
if age < 30 and is_student:
    print("Student discount available")

# OR
if age < 18 or age > 65:
    print("Special pricing")
```

### 📌 Example 6 — Ternary Operator (One-Liner)

```python
# Traditional
age = 20
if age >= 18:
    status = "adult"
else:
    status = "minor"

# One-liner
status = "adult" if age >= 18 else "minor"
print(f"Status: {status}")  # adult
```

---

## 🧪 Practice Exercise

1. Write an `if/else` to check if a number is even or odd
2. Use `if/elif/else` to categorize age: child (0-12), teen (13-19), adult (20-64), senior (65+)
3. Write a nested `if` to check if a number is positive, and if so, whether it's greater than 10
4. Convert an `if/else` to a ternary operator

---

## 📋 Key Takeaways

| Concept | Takeaway |
|---------|----------|
| 🔀 **`if`** | Required — starts every conditional block |
| 🔀 **`elif`** | Optional — check another condition if first was False |
| 🔀 **`else`** | Optional — catch-all for when nothing else matches |
| 📏 **Indentation** | Defines what's inside the block — 4 spaces |
| ⚡ **Ternary** | `value if condition else other` for simple cases |

---

## 🔗 Further Reading

- 📖 [Compound Statements — Official Docs](https://docs.python.org/3/reference/compound_stmts.html#the-if-statement)
- 🌟 [Conditional Expressions — docs](https://docs.python.org/3/reference/expressions.html#conditional-expressions)
- 🧠 [Python Control Flow — W3Schools](https://www.w3schools.com/python/python_conditions.asp)