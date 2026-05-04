# 🎛️ Match-Case: Python's Switch Statement (3.10+)

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square&logo=python" alt="Python 3.10">
  <img src="https://img.shields.io/badge/Match-Clean%20Syntax-green?style=flat-square" alt="Match">
  <img src="https://img.shields.io/badge/Pattern-Matching-orange?style=flat-square" alt="Patterns">
</p>

> ### 💡 Match-case is like a multi-way `if/elif/else` — but cleaner and more powerful for checking exact values.
> Learn Python's modern alternative to long chains of conditions.

---

## 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- ✅ Use `match/case` for cleaner multi-way branching
- ✅ Use the `_` wildcard for default cases
- ✅ Combine patterns with guards for advanced logic

---

## 🧠 Mental Model: A Vending Machine

A vending machine checks your input and picks the matching item:

```
Input: "Coke"  →  Match "Coke"  →  Dispense Coke
Input: "Pepsi" →  Match "Pepsi" →  Dispense Pepsi
Input: ???     →  Match _       →  Error: Unknown
```

Instead of checking each option with `if/elif`, you just list the matches.

---

## 📖 Basic Syntax

```python
match value:
    case "option1":
        print("Chose option 1")
    case "option2":
        print("Chose option 2")
    case _:
        print("Unknown option")  # Default (like else)
```

### Key Rules

1. **`match`** is required — starts the block
2. **`case`** lists each pattern to check
3. **`_`** is the wildcard — catches everything else
4. **First match wins** — stops after finding a match

---

## 📊 `if/elif/else` vs `match/case`

| `if/elif/else` | `match/case` |
|----------------|--------------|
| `if status == "pending":` | `match status:` |
| `    print("Waiting")` | `    case "pending": print("Waiting")` |
| `elif status == "shipped":` | `    case "shipped": print("Shipped")` |
| `    print("On the way")` | `    case _: print("Unknown")` |
| `else: print("Unknown")` | |

> 💡 `match/case` is cleaner when checking **one variable against many values**.

---

## 🌟 Pattern Matching

`match/case` is more than a switch statement — it supports **patterns**:

### 🔹 Multiple Values in One Case

```python
match day:
    case "Saturday" | "Sunday":
        print("Weekend!")
    case _:
        print("Weekday")
```

### 🔹 Guards (Extra Conditions)

```python
match age:
    case n if n < 18:
        print("Minor")
    case n if n < 65:
        print("Adult")
    case _:
        print("Senior")
```

---

## ⚠️ Common Mistakes

```
❌ Using match on Python < 3.10
   match x:  → SyntaxError (requires Python 3.10+)
   Use if/elif/else instead

❌ Forgetting the wildcard
   match color:
       case "red": ...
       case "blue": ...
   # No _ case → unmatched values silently do nothing

❌ Trying to match types (without patterns)
   match x:
       case int: ...    → Won't work as expected
   Use if isinstance(x, int): instead

❌ Using expressions in cases
   case x + 1: ...      → Invalid
   case only supports literals, patterns, and guards
```

---

## 💻 Code Examples

### 📌 Example 1 — Basic Match

```python
status = "shipped"

match status:
    case "pending":
        print("Your order is waiting")
    case "shipped":
        print("Your order is on the way")
    case "delivered":
        print("Your order has arrived")
    case _:
        print("Unknown status")
```

### 📌 Example 2 — Multiple Values

```python
day = "Saturday"

match day:
    case "Saturday" | "Sunday":
        print("Weekend!")
    case "Monday":
        print("Start of the week")
    case "Friday":
        print("Almost weekend")
    case _:
        print("Regular weekday")
```

### 📌 Example 3 — With Guards

```python
score = 85

match score:
    case n if n >= 90:
        print("A")
    case n if n >= 80:
        print("B")
    case n if n >= 70:
        print("C")
    case _:
        print("F")
```

### 📌 Example 4 — HTTP Status Codes

```python
status_code = 404

match status_code:
    case 200:
        print("OK")
    case 301 | 302:
        print("Redirect")
    case 400:
        print("Bad Request")
    case 404:
        print("Not Found")
    case 500:
        print("Server Error")
    case _:
        print("Unknown status")
```

### 📌 Example 5 — Comparing to `if/elif`

```python
# Old way (verbose)
role = "admin"
if role == "admin":
    print("Full access")
elif role == "editor":
    print("Edit access")
elif role == "viewer":
    print("Read-only")
else:
    print("No access")

# New way (clean)
match role:
    case "admin":
        print("Full access")
    case "editor":
        print("Edit access")
    case "viewer":
        print("Read-only")
    case _:
        print("No access")
```

### 📌 Example 6 — Tuple Matching

```python
# Match multiple values at once
point = (3, 5)

match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"On Y-axis at {y}")
    case (x, 0):
        print(f"On X-axis at {x}")
    case (x, y):
        print(f"At point ({x}, {y})")
```

---

## 🧪 Practice Exercise

1. Use `match/case` to convert a number (1-7) to a day name
2. Match a grade letter (A-F) to a message
3. Use the `|` operator to group cases
4. Use a guard to add extra conditions

---

## 📋 Key Takeaways

| Concept | Takeaway |
|---------|----------|
| 🎛️ **`match/case`** | Cleaner than long `if/elif` chains for exact values |
| 🔹 **`_` wildcard** | Catches everything — like `else` |
| 🔹 **`|` operator** | Match multiple values in one case |
| 🛡️ **Guards** | Add extra conditions with `if` |
| 🐍 **Python 3.10+** | Required — not available in older versions |

---

## 🔗 Further Reading

- 📖 [Structural Pattern Matching — Official Docs](https://docs.python.org/3/reference/compound_stmts.html#the-match-statement)
- 🎛️ [PEP 636 — Match Statement Tutorial](https://peps.python.org/pep-0636/)
- 🧠 [Pattern Matching in Depth — Real Python](https://realpython.com/python-match-case-statement/)