# ✨ Decorators: Enhancing Functions

<p align="center">
  <img src="https://img.shields.io/badge/%40-Syntax-blue?style=flat-square" alt="@">
  <img src="https://img.shields.io/badge/Wrapper-Function%20Wrapping-green?style=flat-square" alt="Wrapper">
  <img src="https://img.shields.io/badge/Crosscutting-Logging%2FAuth-orange?style=flat-square" alt="Crosscutting">
</p>

> ### 💡 Decorators are like gift wrapping — they add extra behavior to functions without changing the function itself.
> Learn how to use and create decorators to enhance your code.

---

## 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- ✅ Understand what decorators do and why they're useful
- ✅ Use built-in decorators like `@staticmethod` and `@property`
- ✅ Create your own custom decorators

---

## 🧠 Mental Model: A Gift Wrapper

A decorator is like **wrapping a gift**:

```
🎁 Original function = The gift
📦 Decorator = The wrapping paper
   → Gift stays the same, but now it has extra features!
```

The decorator takes a function, adds behavior, and returns a new enhanced function.

---

## 📖 Basic Syntax

```python
@decorator_name
def my_function():
    pass

# Same as:
def my_function():
    pass
my_function = decorator_name(my_function)
```

---

## 📊 Common Built-in Decorators

| Decorator | What it does | Use case |
|-----------|-------------|----------|
| `@property` | Turns method into attribute | Getters/setters |
| `@staticmethod` | No `self` needed | Utility methods |
| `@classmethod` | Gets class as first arg | Factory methods |
| `@lru_cache` | Caches results | Speed up repeated calls |

---

## ⚠️ Common Mistakes

```
❌ Forgetting to return the wrapper
   def my_decorator(func):
       def wrapper():
           print("Before")
           func()
           # Missing return wrapper!
       return wrapper

❌ Not using @wraps
   @wraps(func) preserves original function name and docstring
   Without it, decorated function shows as "wrapper"

❌ Decorators with arguments complexity
   @decorator(arg) requires THREE nested functions!
   def decorator(arg):
       def outer(func):
           def wrapper(*args, **kwargs):
               ...
           return wrapper
       return outer

❌ Overusing decorators
   Simple code doesn't need decoration
   Use only when behavior is truly reusable
```

---

## 💻 Code Examples

### 📌 Example 1 — Simple Decorator

```python
def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# Before function call
# Hello!
# After function call
```

### 📌 Example 2 — Decorator with Arguments

```python
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
```

### 📌 Example 3 — Timing Decorator

```python
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end-start:.4f}s")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(0.1)
    return "Done!"

slow_function()
```

### 📌 Example 4 — Logging Decorator

```python
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@logger
def add(a, b):
    return a + b

add(3, 5)
```

### 📌 Example 5 — Preserving Metadata

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)  # Preserves name and docstring
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def greet(name):
    """Greets a person."""
    print(f"Hi, {name}!")

print(greet.__name__)  # greet (not wrapper!)
print(greet.__doc__)   # Greets a person.
```

### 📌 Example 6 — Class Decorator

```python
def singleton(cls):
    """Ensures only one instance of a class exists."""
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class Database:
    def __init__(self):
        print("Database created!")

db1 = Database()
db2 = Database()
print(db1 is db2)  # True (same instance)
```

---

## 🧪 Practice Exercise

1. Create a decorator that prints "Starting" and "Finished" around any function
2. Create a decorator that retries a function if it fails
3. Use `@wraps` to preserve function metadata
4. Create a decorator that caches function results

---

## 📋 Key Takeaways

| Concept | Takeaway |
|---------|----------|
| ✨ **Decorator** | Function that wraps another function |
| 🎯 **`@` syntax** | Clean way to apply decorators |
| 📦 **Wrapper** | Inner function that adds behavior |
| 🔒 **`@wraps`** | Preserves original function metadata |
| 🔄 **Arguments** | Decorators with args need 3 levels of nesting |

---

## 🔗 Further Reading

- 📖 [Decorators — Official Docs](https://docs.python.org/3/glossary.html#term-decorator)
- 🌟 [Primer on Decorators — Real Python](https://realpython.com/primer-on-python-decorators/)
- 🔧 [functools.wraps — docs](https://docs.python.org/3/library/functools.html#functools.wraps)