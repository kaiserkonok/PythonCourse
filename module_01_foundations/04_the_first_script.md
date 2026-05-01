# The First Script: Understanding print() and Execution Flow

## Learning Objectives

- Understand what print() does and how to use it
- Learn the execution flow of a Python script
- Understand how Python reads and processes code line by line

## The print() Function

`print()` is a **function** - a reusable piece of code that does a specific task.

- **Task:** Display text or values on the screen
- **Syntax:** print("your message") or print(your_variable)

```
┌─────────────────────────────────────┐
│        print("Hello!")                │
│                                     │
│   Output:  Hello!                   │
└─────────────────────────────────────┘
```

### What's Inside the Parentheses?

- **"Hello!"** = The argument (the data you want to print)
- Can be:
  - Text: "Hello"
  - Numbers: 42
  - Variables: name
  - Results: 2 + 3

## Execution Flow: How Python Runs Your Code

Python reads your code **top to bottom, left to right**:

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

## Code Examples

```python
# Example 1: Basic print
print("Hello, World!")

# Example 2: Print numbers (no quotes needed)
print(42)
print(3.14159)

# Example 3: Print calculations
print(10 + 5)        # Output: 15
print("5" + "5")      # Output: 55 (string concatenation)

# Example 4: Print variables
message = "Learning Python!"
print(message)

# Example 5: Multiple prints
print("First")
print("Second")
print("Third")

# Example 6: f-strings (formatted strings)
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old")
```

## Understanding Execution Order

```python
# 1. Python assigns "Alice" to the variable 'name'
name = "Alice"

# 2. Python assigns 25 to the variable 'age'
age = 25

# 3. Python evaluates the calculation (25 + 5 = 30)
future_age = age + 5

# 4. Finally, Python executes print()
print(f"{name} will be {future_age} in 5 years")

# Output: Alice will be 30 in 5 years
```

## Keyword Arguments in print()

```python
# end parameter - changes what prints at the end
print("Hello", end=" ")
print("World")
# Output: Hello World

# sep parameter - changes separator between items
print("Python", "is", "fun", sep="-")
# Output: Python-is-fun

# Multiple parameters
print("A", "B", "C", sep=" → ")
# Output: A → B → C
```

## Key Takeaways

1. **print()** displays output to the screen
2. **Execution is linear** - code runs from top to bottom
3. **Variables** store data for later use
4. **f-strings** combine text and variables cleanly
5. **Arguments** customize print() behavior (end, sep)

## Practice Exercise

Create a script that:
1. Has 3 variables: your name, your age, your city
2. Prints each on a separate line
3. Adds 10 to your age and prints the result

Example output:
```
My name is Alice
My age is 25
I live in New York
In 10 years, I will be 35
```