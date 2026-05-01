# Dynamic Typing: How Python Manages Types Automatically

## Learning Objectives

- Understand dynamic typing vs static typing
- Learn how Python determines types at runtime
- Create flexible code using dynamic typing

## What is Dynamic Typing?

In Python, **you don't declare variable types** - Python figures it out automatically.

```python
# No type declaration needed!
x = 10        # Python knows x is an int
x = "hello"   # Now x is a string - completely fine!
```

This is different from many other languages:

```python
# Java (static typing) - you MUST declare type
int x = 10;
String x = "hello";  // ERROR! Can't reuse variable name

# Python (dynamic typing) - no declaration needed
x = 10        # x is now an int
x = "hello"   # x is now a string - totally fine!
```

## How Python Handles Types

Python tracks types at **runtime** (when code executes):

```python
x = 10
print(type(x))  # <class 'int'>

x = "hello"
print(type(x))  # <class 'str'>
```

```
┌─────────────────────────────────────┐
│  Dynamic Typing in Action           │
│                                      │
│  x = 10     → type: int             │
│  x = "hello"→ type: str              │
│  x = [1,2]  → type: list            │
│                                      │
│  Type changes as you assign new     │
│  values - Python handles it all!    │
└─────────────────────────────────────┘
```

## Benefits and Drawbacks

### Benefits

| Benefit | Example |
|---------|---------|
| Less code to write | No type declarations |
| More flexibility | Change types easily |
| Faster prototyping | Try different approaches |
| Beginner-friendly | Focus on logic, not syntax |

### Drawbacks

| Drawback | Example |
|----------|---------|
| Less error checking | Bugs caught later |
| Harder to read code | Unclear what type expected |
| Slower performance | Type checked at runtime |

## Best Practices

```python
# ✅ Good: Clear variable names indicate expected type
user_name = "Alice"       # String
user_count = 10           # Integer
is_active = True         # Boolean

# ❌ Bad: Unclear names obscure type intent
x = "Alice"
y = 10
z = True

# ⚠️ Use type hints (Python 3.5+)
# This documents intent while keeping flexibility
name: str = "Alice"
age: int = 25
is_active: bool = True
```

## Code Examples

```python
# Example 1: Type changes automatically
value = 10
print(type(value))  # int

value = "hello"
print(type(value))  # str

value = 3.14
print(type(value))  # float

# Example 2: Function returns different types
def get_result(value):
    if value > 10:
        return "Big"      # String
    else:
        return 0           # Integer (different type!)

print(get_result(5))    # 0
print(get_result(15))  # Big

# Example 3: Type hints (optional but helpful)
def greet(name: str) -> str:
    return f"Hello, {name}!"

print(greet("Alice"))

# Example 4: Checking types at runtime
x = "hello"
if isinstance(x, str):
    print(f"x is a string: {x.upper()}")
```

## Key Takeaways

1. **Dynamic typing** - Python determines types automatically
2. **No declarations needed** - Just assign values
3. **Types can change** - Variable type changes with new value
4. **Type hints** - Optional way to document intent
5. **Trade-off** - Less code but potentially more bugs

## Practice Exercise

1. Create a variable with an integer
2. Print its type
3. Change it to a string
4. Print its type again
5. Use a type hint for a variable and see how it behaves