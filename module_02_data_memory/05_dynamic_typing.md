# Dynamic Typing: How Python Manages Types Automatically

## Learning Objectives

By the end of this lesson, you will be able to:

- Understand the difference between dynamic and static typing
- See how Python tracks types at runtime
- Use type hints to document your code

---

## Mental Model: The Chameleon

In languages like Java or C++, you declare the type of every variable:

```java
// Java (static typing) — type must be declared
int x = 10;        // x is an integer
String name = "hi"; // name is a string
```

In Python, the variable doesn't have a type — **the value does**:

```python
# Python (dynamic typing) — type is inferred
x = 10          # Python sees: x points to an int
x = "hello"     # Python sees: x now points to a string
x = 3.14        # Python sees: x now points to a float
```

Python is like a **chameleon** — it adapts to whatever value you give it.

---

## Dynamic vs Static: The Trade-off

| Aspect | Dynamic (Python) | Static (Java, C++) |
|--------|------------------|-------------------|
| **Declare types?** | No | Yes |
| **Type errors** | Caught at runtime | Caught before running |
| **Flexibility** | High — change types anytime | Low — type is fixed |
| **Speed** | Slightly slower | Faster |
| **Beginner-friendly?** | ✅ Yes | ❌ More to learn |

### What This Means for You

```python
# In Python, you focus on what you want to do — not the type system
name = "Alice"      # String
name = 123           # Now it's an int
name = [1, 2, 3]    # Now it's a list

# Python doesn't care. It just works.
```

---

## How Python Tracks Types

Python stores the **type with the value**, not the variable:

```python
x = 10
print(type(x))  # <class 'int'>

x = "hello"
print(type(x))  # <class 'str'>

x = [1, 2, 3]
print(type(x))  # <class 'list'>
```

The variable `x` is just a label. The type belongs to what `x` points to.

---

## Common Mistakes

```
❌ Assuming a variable keeps its type
   x = 10        # x is int
   x = "hello"   # x is now str — no warning!

❌ Not knowing type hints exist (Python 3.5+)
   x: int = 10   ← This documents intent but doesn't enforce it

❌ Using type() in production code for logic
   if type(x) == int:     ← Not Pythonic
   if isinstance(x, int): ← Better
```

---

## Code Examples

### Example 1 — Type Changes Automatically

```python
value = 10
print(type(value))  # <class 'int'>

value = "hello"
print(type(value))  # <class 'str'>

value = 3.14
print(type(value))  # <class 'float'>
```

### Example 2 — Function Returns Different Types

```python
def get_result(value):
    """Returns a string for large values, int for small."""
    if value > 10:
        return "Big"      # String
    else:
        return 0          # Integer

print(get_result(5))     # 0 (int)
print(get_result(15))    # Big (str)
```

### Example 3 — Type Hints (Optional)

Type hints document what type a variable **should** be. Python ignores them at runtime — they're for humans and tools:

```python
def greet(name: str) -> str:
    """name: str means 'name should be a string'."""
    """-> str means 'this function returns a string'."""
    return f"Hello, {name}!"

print(greet("Alice"))  # Hello, Alice!
```

### Example 4 — Checking Types at Runtime

```python
x = "hello"

# Using isinstance() — the Pythonic way
if isinstance(x, str):
    print(f"x is a string: {x.upper()}")

# You can check multiple types
y = 10
if isinstance(y, (int, float)):
    print(f"y is a number: {y}")
```

### Example 5 — When Dynamic Typing Bites You

```python
# A common bug: mixing types accidentally
def add_values(a, b):
    """Expects two numbers, but Python won't stop strings."""
    return a + b

# This works:
print(add_values(10, 5))      # 15 (int addition)
print(add_values(3.14, 2))    # 5.14 (float addition)

# But this also "works" — maybe not what you intended:
print(add_values("10", "5"))  # "105" (string concatenation!)
```

---

## Best Practices

```python
# ✅ Use clear variable names that indicate type
user_name = "Alice"       # Clearly a string
user_count = 10           # Clearly an int
is_active = True          # Clearly a boolean

# ✅ Use type hints for functions
def calculate_total(price: float, quantity: int) -> float:
    return price * quantity

# ✅ Use isinstance() for type checking
if isinstance(x, str):
    print(x.upper())
```

---

## Practice Exercise

1. Create a variable with an integer
2. Print its type
3. Change it to a string
4. Print its type again
5. Use a type hint for a variable and see how it behaves

---

## Key Takeaways

- **Dynamic typing** means Python figures out types automatically
- **Variables don't have types** — values do
- **Type hints** document intent but don't enforce anything
- **isinstance()** is the Pythonic way to check types
- **Trade-off**: less code but fewer safety checks

---

## Further Reading

- [Python Type Hints — Official Docs](https://docs.python.org/3/library/typing.html)
- [Dynamic vs Static Typing — Real Python](https://realpython.com/python-type-checking/)
- [Mypy — Type Checker for Python](https://mypy.readthedocs.io/) — Add type checking to Python