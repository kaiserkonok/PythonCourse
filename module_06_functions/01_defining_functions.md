# 🛠️ Defining Functions: Reusable Code Blocks

<p align="center">
  <img src="https://img.shields.io/badge/def-Define-blue?style=flat-square" alt="def">
  <img src="https://img.shields.io/badge/return-Output-green?style=flat-square" alt="return">
  <img src="https://img.shields.io/badge/DRY-Don't%20Repeat%20Yourself-orange?style=flat-square" alt="DRY">
</p>

> ### 💡 Functions are like recipes — you write them once, then use them whenever you need the result. No copy-pasting, just call and go.
> Learn how to create reusable blocks of code.

---

## 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- ✅ Define and call functions using `def`
- ✅ Return values from functions
- ✅ Understand the difference between printing and returning

---

## 🧠 Mental Model: A Coffee Machine

A function is like a **coffee machine**:

```
Input:  [Coffee beans] + [Water]
Process: [Grind] → [Brew] → [Filter]
Output: ☕ [Fresh coffee]
```

You don't need to know how it works inside — you just press a button and get your result.

---

## 📖 Basic Syntax

```python
def function_name(parameters):
    """Docstring: explains what the function does."""
    # Body: the code that runs
    return result  # Optional
```

### Key Rules

1. **`def`** starts every function definition
2. **Name** should be lowercase with underscores (`my_function`)
3. **`()`** holds parameters (inputs)
4. **`:`** ends the definition line
5. **Indentation** defines the function body

---

## 📊 Print vs Return

| Print | Return |
|-------|--------|
| Shows output to user | Sends value back to caller |
| Result is lost | Result can be stored or used |
| For debugging/display | For logic/computation |

```python
def add_print(a, b):
    print(a + b)  # Just shows it

def add_return(a, b):
    return a + b  # Sends it back

x = add_print(2, 3)   # Output: 5
print(x)              # Output: None (nothing returned!)

y = add_return(2, 3)  # No output
print(y)              # Output: 5 (value was returned!)
```

---

## ⚠️ Common Mistakes

```
❌ Forgetting the parentheses
   def greet:      → SyntaxError
   def greet():    ← Correct

❌ Forgetting the colon
   def greet()
       print("Hi") → SyntaxError
   def greet():
       print("Hi") ← Correct

❌ Confusing print and return
   def double(x):
       print(x * 2)   ← Shows value, returns None
   def double(x):
       return x * 2   ← Returns value, doesn't show

❌ Defining inside a loop
   for i in range(10):
       def foo(): ...  ← Redefines every iteration!
```

---

## 💻 Code Examples

### 📌 Example 1 — Simple Function

```python
def greet():
    """Prints a greeting message."""
    print("Hello, World!")

greet()  # Call the function
```

### 📌 Example 2 — Function with Parameters

```python
def greet(name):
    """Greets a specific person."""
    print(f"Hello, {name}!")

greet("Alice")  # Hello, Alice!
greet("Bob")    # Hello, Bob!
```

### 📌 Example 3 — Returning Values

```python
def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

result = add(5, 3)
print(f"Sum: {result}")  # Sum: 8
```

### 📌 Example 4 — Multiple Returns

```python
def get_stats(numbers):
    """Returns min, max, and average."""
    return min(numbers), max(numbers), sum(numbers) / len(numbers)

low, high, avg = get_stats([10, 20, 30, 40])
print(f"Low: {low}, High: {high}, Avg: {avg}")
```

### 📌 Example 5 — No Return (Implicit None)

```python
def log_message(msg):
    """Just prints, doesn't return anything."""
    print(f"LOG: {msg}")

result = log_message("Starting...")
print(f"Returned: {result}")  # Returned: None
```

### 📌 Example 6 — Function as Variable

```python
def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

# Assign function to variable
speak = shout
print(speak("Hello"))  # HELLO

# Pass function as argument
def process(text, func):
    return func(text)

print(process("Hello", whisper))  # hello
```

---

## 🧪 Practice Exercise

1. Define a function that takes a name and returns a greeting
2. Create a function that calculates the area of a circle
3. Write a function that returns multiple values (e.g., square and cube)
4. Create a function that prints a pattern

---

## 📋 Key Takeaways

| Concept | Takeaway |
|---------|----------|
| 🛠️ **`def`** | Starts every function definition |
| 🔙 **`return`** | Sends a value back to the caller |
| 🖨️ **`print` vs `return`** | `print` shows output, `return` gives value |
| 🔄 **Reusable** | Define once, call many times |
| 📝 **Docstrings** | Explain what the function does |

---

## 🔗 Further Reading

- 📖 [Defining Functions — Official Docs](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- 🌟 [Functions — Real Python](https://realpython.com/defining-your-own-python-function/)
- 📚 [Docstrings — PEP 257](https://peps.python.org/pep-0257/)