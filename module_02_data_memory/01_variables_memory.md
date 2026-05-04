# 🏷️ Variables & Memory Labels: How Data is Stored and Referenced

<p align="center">
  <img src="https://img.shields.io/badge/Concept-Variables-blue?style=flat-square" alt="Variables">
  <img src="https://img.shields.io/badge/Convention-snake__case-green?style=flat-square" alt="snake_case">
  <img src="https://img.shields.io/badge/Skill-Foundational-orange?style=flat-square" alt="Foundational">
</p>

> ### 💡 Variables are not boxes — they're labels. When you write x = 10, you stick a label called "x" onto the number 10.
> Learn how Python stores data in memory and how to name your variables like a pro.

---

## 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- ✅ Understand what variables are and how they work in memory
- ✅ Follow Python's naming conventions like a pro
- ✅ Use the assignment operator correctly (and avoid common mistakes)

---

## 🧠 Mental Model: Post-it Notes

Variables in Python are **not boxes** — they're **labels** or **post-it notes**.

When you write `x = 10`:
- You don't put 10 inside x
- You stick a label called "x" onto the number 10

```
   10  ← The actual data (lives in RAM)
   ↑
  [x]  ← The label (variable name)
```

When you reassign `x = 20`:
- You don't replace the value — you move the label
- The old value (10) sits there (Python cleans it up later)

```
   20  ← New data
   ↑
  [x]  ← Label moved here

   10  ← Old data (waiting to be cleaned up)
```

> 💡 **Key insight:** Variables are labels that point to data. They're not containers.

---

## 📖 Creating Variables

In Python, you create a variable by **assigning** a value to a name using `=`:

```python
name = "Alice"
age = 25
is_student = True
```

The `=` symbol is called the **assignment operator**. It means:

> "Take the value on the right and attach the name on the left."

> ⚠️ It does NOT mean "equals" like in math.

---

## 📝 Variable Naming Rules

Python enforces some rules — and conventions — for naming variables.

### 🚨 Rules (Python will crash if you break these)

| Rule | ✅ Correct | ❌ Incorrect |
|------|-----------|-------------|
| Start with letter or underscore | `name`, `_value` | `2name` |
| Only letters, numbers, underscores | `user_name` | `user-name` |
| Can't be a Python keyword | `score` | `if`, `for`, `while` |
| No spaces | `my_value` | `my value` |

### 💡 Conventions (Python won't crash — but other developers will judge you)

| Style | Example | Pythonic? |
|-------|---------|-----------|
| 🟢 snake_case | `user_name`, `first_name` | ✅ Yes — this is Python convention |
| 🟡 camelCase | `userName`, `firstName` | ⚠️ Less Pythonic |
| 🔴 PascalCase | `UserName`, `FirstName` | ⚠️ Only for class names |

### 🎯 What's a Good Variable Name?

```python
# ❌ Bad — what does 'x' even mean?
x = 25
y = "Alice"

# ✅ Good — crystal clear what each variable holds
age = 25
name = "Alice"
```

---

## ⚠️ Common Mistakes

```
❌ Using a variable before defining it
   print(age)    → NameError
   age = 25      ← Define it first!

❌ Using = for comparison
   if x = 10:    → SyntaxError (use == instead)

❌ Using Python keywords as variable names
   class = "A"   → SyntaxError (class is a keyword)
   Class = "A"   ← Works but not Pythonic (PascalCase is for classes)

❌ Using camelCase when you should use snake_case
   userName      ← Works, but Python convention is user_name
```

---

## 💻 Code Examples

### 📌 Example 1 — Creating Variables

```python
# Create a variable and print it
player_name = "Mario"
print(player_name)  # Output: Mario
```

### 📌 Example 2 — Reassigning Variables

```python
# Variables can change their value
age = 25
print(age)       # 25

age = 26          # Reassign the variable
print(age)       # 26 (old value is gone)
```

### 📌 Example 3 — Multiple Variables

```python
# Multiple variables in one script
x = 5
y = 10
z = x + y
print(z)  # Output: 15
```

### 📌 Example 4 — Multiple Assignment

```python
# Python lets you assign multiple variables at once
a, b, c = 1, 2, 3
print(a, b, c)  # 1 2 3

# Swap values (Python magic!)
x = 10
y = 20
x, y = y, x      # No temp variable needed
print(f"x = {x}, y = {y}")  # x = 20, y = 10
```

### 📌 Example 5 — Checking a Variable's Type

```python
# Every variable has a type — Python tracks it for you
age = 25
name = "Alice"
is_student = True

print(type(age))        # <class 'int'>
print(type(name))       # <class 'str'>
print(type(is_student))  # <class 'bool'>
```

---

## 🧪 Practice Exercise

Create variables for:

1. Your first name (string)
2. Your last name (string)
3. Your age (integer)
4. Whether you like programming (boolean)

Print them all on one line using an f-string.

---

## 📋 Key Takeaways

| Concept | Takeaway |
|---------|----------|
| 🏷️ **Variables are labels** | They point to data, they're not containers |
| 🟰 **The `=` operator** | Assigns a value to a name (it's not mathematical equality) |
| 🐍 **Snake_case is the Python convention** | Use `user_name`, not `userName` |
| 🎯 **Good names matter** | `age = 25` is clearer than `x = 25` |
| 🔄 **Reassignment changes** | The label's target — the old value is cleaned up |

---

## 🔗 Further Reading

- 📖 [Python Naming Conventions — PEP 8](https://peps.python.org/pep-0008/#naming-conventions) — Official style guide
- 🏷️ [Variables in Python — Real Python](https://realpython.com/python-variables/) — Deep dive
- 🔧 [Python Built-in Functions — docs](https://docs.python.org/3/library/functions.html) — Complete reference