# Error & Exception Handling: Using try/except to Prevent Program Crashes

## Learning Objectives

- Understand the difference between errors and exceptions
- Use try/except to handle errors
- Create custom exceptions

## What are Exceptions?

Exceptions are **errors that occur while code runs**:

- Division by zero
- File not found
- Invalid type

```python
# This causes an error!
result = 10 / 0
```

## Basic try/except

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

## The Exception Hierarchy

```
Exception (base)
├── ZeroDivisionError
├── ValueError
├── TypeError
├── FileNotFoundError
└── ... (many more)
```

## Code Examples

```python
# Example 1: Basic try/except
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Example 2: Multiple exceptions
try:
    value = int("hello")
except ValueError:
    print("Invalid value")
except TypeError:
    print("Wrong type")

# Example 3: Catch all exceptions
try:
    result = 10 / 0
except Exception as e:
    print(f"Error: {e}")

# Example 4: Try/except/else
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print(f"Result: {result}")  # Runs if no error

# Example 5: Try/except/finally (always runs)
try:
    file = open("file.txt")
    content = file.read()
except FileNotFoundError:
    print("File not found")
finally:
    print("Cleanup complete")  # Always runs
```

## Raising Exceptions

```python
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

try:
    divide(10, 0)
except ValueError as e:
    print(e)  # Cannot divide by zero!
```

## Custom Exceptions

```python
class InvalidAgeError(Exception):
    pass

def set_age(age):
    if age < 0:
        raise InvalidAgeError("Age cannot be negative!")
    return age

try:
    set_age(-5)
except InvalidAgeError as e:
    print(e)
```

## Key Takeaways

1. **try** - code that might fail
2. **except** - handle the error
3. **else** - runs if no error
4. **finally** - always runs (cleanup)
5. **raise** - create your own errors

## Practice Exercise

1. Handle division by zero
2. Handle invalid input conversion
3. Use try/except/finally
4. Create a custom exception