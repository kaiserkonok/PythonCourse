# The First Script: Understanding print() and Execution Flow

## Learning Objectives

By the end of this lesson, you will be able to:

- Use `print()` to display text, numbers, and variables
- Understand how Python reads and executes code line by line
- Customize output with f-strings and print() parameters

---

## Mental Model: The Assembly Line

Think of your Python script as an **assembly line**:

1. Line 1 runs first
2. Line 2 runs second
3. Line 3 runs third
4. And so on...

Python reads your code **top to bottom, left to right** — exactly in the order you wrote it. If line 3 depends on line 1, line 1 must run first.

---

## The print() Function

`print()` is a **built-in function** — it's already part of Python, ready to use.

**What it does:** Displays output on the screen.

**What you give it:** Anything you want to display.

```
┌─────────────────────────────────────┐
│  print("Hello!")                    │
│       └───┬───┘                     │
│           │                         │
│   What you want to display         │
│                                     │
│   Output:  Hello!                  │
└─────────────────────────────────────┘
```

### What Can print() Handle?

| Input | Code | Output |
|-------|------|--------|
| Text | `print("hello")` | hello |
| Number | `print(42)` | 42 |
| Variable | `print(name)` | Alice |
| Math | `print(2 + 3)` | 5 |
| Multiple | `print("Hi", 5)` | Hi 5 |

---

## Execution Flow: How Python Reads Your Code

Python is a **sequential** language. It reads your code from top to bottom:

```python
# Line 1: This runs FIRST
print("Step 1")

# Line 2: This runs SECOND
print("Step 2")

# Line 3: This runs THIRD
print("Step 3")

# Output:
# Step 1
# Step 2
# Step 3
```

```
┌─────────────────────────────────────┐
│  Code Flow in Python                │
│                                     │
│  Line 1 ──→ Line 2 ──→ Line 3      │
│    ↓          ↓          ↓          │
│  Execute   Execute   Execute       │
└─────────────────────────────────────┘
```

**Important:** If you put `print(y)` before `y = 10`, Python will crash because `y` doesn't exist yet.

---

## f-strings: Embedding Variables in Text

An **f-string** lets you put variables directly inside a string:

```python
name = "Alice"
age = 25

# Without f-string (the old way — ugly)
print("My name is " + name + " and I am " + str(age) + " years old")

# With f-string (the Pythonic way — clean)
print(f"My name is {name} and I am {age} years old")
```

The `f` before the quotes tells Python: "look for variables inside `{curly braces}` and replace them."

### What You Can Put Inside `{}`

```python
name = "Alice"
age = 25

# Variables
print(f"My name is {name}")

# Math
print(f"Double my age: {age * 2}")

# Methods
print(f"Name in uppercase: {name.upper()}")

# Calculations
print(f"Next year I'll be {age + 1}")
```

---

## print() Parameters: Customizing Output

`print()` has extra settings called **parameters**:

### `end` — What prints at the end

By default, `print()` adds a newline (`\n`). You can change that:

```python
print("Hello", end=" ")
print("World")
# Output: Hello World (on the same line!)
```

### `sep` — How to separate multiple items

By default, `print()` separates items with a space:

```python
print("Python", "is", "fun")
# Output: Python is fun

# Change the separator
print("Python", "is", "fun", sep="-")
# Output: Python-is-fun
```

---

## Common Mistakes

```
❌ Forgetting quotes around text
   print(Hello)    → NameError
   print("Hello")  → Correct

❌ Using print() before defining a variable
   print(x)        → NameError (x doesn't exist yet)
   x = 10
   print(x)        → Correct

❌ Confusing + for numbers and strings
   print("5" + "5")  → "55" (concatenation)
   print(5 + 5)      → 10 (addition)

❌ Missing the f before the string
   name = "Alice"
   print("{name}")    → Prints {name} literally
   print(f"{name}")   → Prints Alice (correct!)
```

---

## Code Examples

### Example 1 — Basic print()

```python
# Simple text output
print("Hello, World!")
# Output: Hello, World!
```

### Example 2 — Print Numbers

```python
# No quotes needed for numbers
print(42)          # Output: 42
print(3.14159)     # Output: 3.14159
print(-100)        # Output: -100
```

### Example 3 — Print Calculations

```python
# Python evaluates the math first
print(10 + 5)       # Output: 15
print(10 * 3)       # Output: 30
print(100 / 4)      # Output: 25.0
```

### Example 4 — Print Variables

```python
# Store a value, then print it
message = "Learning Python!"
print(message)
# Output: Learning Python!
```

### Example 5 — f-strings

```python
name = "Alice"
age = 25
city = "New York"

print(f"My name is {name}")
print(f"I am {age} years old")
print(f"I live in {city}")
print(f"Next year I'll be {age + 1}")
# Output:
# My name is Alice
# I am 25 years old
# I live in New York
# Next year I'll be 26
```

### Example 6 — Customizing print()

```python
# end parameter — no newline
print("Hello", end=" ")
print("World")
# Output: Hello World

# sep parameter — custom separator
print("Python", "is", "fun", sep="-")
# Output: Python-is-fun

# Both together
print("A", "B", "C", sep=" → ", end="!\n")
# Output: A → B → C!
```

---

## Practice Exercise

Create a script that:

1. Creates 3 variables: your name, your age, your city
2. Prints each on a separate line
3. Uses an f-string to show what your age will be in 10 years

**Expected output:**
```
My name is Alice
My age is 25
I live in New York
In 10 years, I will be 35
```

---

## Key Takeaways

- **print()** displays output on the screen
- **Execution is sequential** — Python runs your code top to bottom
- **Variables must be defined** before you use them
- **f-strings** let you embed variables inside text with `{curly braces}`
- **end and sep** parameters customize how print() formats output

---

## Further Reading

- [Python print() Documentation](https://docs.python.org/3/library/functions.html#print) — Official reference
- [f-strings — Real Python](https://realpython.com/python-f-strings/) — Deep dive into f-strings
- [Python Execution Model](https://docs.python.org/3/reference/executionmodel.html) — How Python runs code