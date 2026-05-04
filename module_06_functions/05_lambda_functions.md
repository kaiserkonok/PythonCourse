# ⚡ Lambda Functions: Anonymous One-Liners

<p align="center">
  <img src="https://img.shields.io/badge/lambda-Anonymous-blue?style=flat-square" alt="lambda">
  <img src="https://img.shields.io/badge/Short-One%20Line-green?style=flat-square" alt="one-line">
  <img src="https://img.shields.io/badge/Use-Callbacks%20%26%20Sorting-orange?style=flat-square" alt="Use Case">
</p>

> ### 💡 Lambda functions are quick, anonymous functions for simple tasks. Like a sticky note — small, temporary, and perfect for one-time use.
> Learn how to write inline functions without naming them.

---

## 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- ✅ Create lambda functions using the `lambda` keyword
- ✅ Use lambdas with `sorted()`, `map()`, and `filter()`
- ✅ Know when to use lambdas vs regular functions

---

## 🧠 Mental Model: A Sticky Note

A lambda is like a **sticky note** — you write a quick instruction and stick it where needed:

```
Regular function:  "Here's a formal recipe card"
Lambda function:   "Here's a quick sticky note: 'sort by name'"
```

Lambdas are for **small, throwaway** functions that you only use once.

---

## 📖 The Syntax

```python
lambda arguments: expression
```

| Part | What it is |
|------|------------|
| `lambda` | Keyword |
| `arguments` | Input variables (like function parameters) |
| `:` | Separator |
| `expression` | The result (automatically returned) |

---

## 📊 Lambda vs Regular Function

```python
# Regular function
def add(a, b):
    return a + b

# Lambda
add = lambda a, b: a + b

# Both do the same thing!
```

---

## ⚠️ Common Mistakes

```
❌ Multiple expressions
   lambda x: x + 1; x * 2  → SyntaxError
   Lambdas can only have ONE expression

❌ Statements inside lambdas
   lambda x: if x > 0: x  → SyntaxError
   Lambdas can't contain statements (if, for, while, etc.)

❌ Overcomplicating lambdas
   lambda x: ...  # 50 characters of logic
   ← Use a regular function instead

❌ Not assigning or using
   lambda x: x + 1  ← Does nothing! Must use immediately
   sorted(items, key=lambda x: x.name)  ← Correct
```

---

## 💻 Code Examples

### 📌 Example 1 — Basic Lambda

```python
# Regular function
def square(x):
    return x ** 2

# Lambda equivalent
square = lambda x: x ** 2

print(square(5))  # 25
```

### 📌 Example 2 — Multiple Arguments

```python
add = lambda a, b: a + b
print(add(3, 4))  # 7
```

### 📌 Example 3 — Sorting with Lambda

```python
students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92},
    {"name": "Charlie", "grade": 78}
]

# Sort by grade
sorted_students = sorted(students, key=lambda s: s["grade"])
print(sorted_students)
```

### 📌 Example 4 — `map()` with Lambda

```python
numbers = [1, 2, 3, 4, 5]

# Square each number
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # [1, 4, 9, 16, 25]
```

### 📌 Example 5 — `filter()` with Lambda

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Keep only even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4, 6, 8, 10]
```

### 📌 Example 6 — Immediate Invocation

```python
# Lambda called immediately
result = (lambda x, y: x + y)(3, 4)
print(result)  # 7
```

---

## 🧪 Practice Exercise

1. Create a lambda that multiplies two numbers
2. Use a lambda to sort a list of tuples by the second element
3. Filter a list of words to only include those longer than 5 characters
4. Use `map()` with a lambda to convert strings to uppercase

---

## 📋 Key Takeaways

| Concept | Takeaway |
|---------|----------|
| ⚡ **Lambda** | Anonymous one-line function |
| 📏 **Syntax** | `lambda args: expression` |
| 🔄 **Use cases** | `sorted()`, `map()`, `filter()` |
| 📝 **Limitations** | One expression only, no statements |
| 🎯 **When to use** | Simple, throwaway logic — not complex functions |

---

## 🔗 Further Reading

- 📖 [Lambda Expressions — Official Docs](https://docs.python.org/3/reference/expressions.html#lambda)
- 🌟 [Map, Filter, Lambda — Real Python](https://realpython.com/python-lambda/)
- 🔧 [Functional Programming — docs](https://docs.python.org/3/howto/functional.html)