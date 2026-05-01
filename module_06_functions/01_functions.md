# Defining Functions: Encapsulating Logic for Reusability

## Learning Objectives

- Create and call functions
- Understand function structure
- Return values from functions

## What is a Function?

A function is a **reusable block** of code:

- Defined once
- Called any number of times
- Can accept input and return output

```python
def greet():
    print("Hello!")

greet()  # Call the function
```

## Function Structure

```
def function_name(parameters):
    # Code block
    return value  # Optional
```

```python
def greet(name):
    return f"Hello, {name}!"

message = greet("Alice")
print(message)  # Hello, Alice!
```

## Code Examples

```python
# Example 1: Simple function
def say_hello():
    print("Hello!")

say_hello()  # Hello!

# Example 2: Function with parameter
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # Hello, Alice!
greet("Bob")   # Hello, Bob!

# Example 3: Function returning value
def add(a, b):
    return a + b

result = add(3, 5)
print(result)  # 8

# Example 4: Multiple parameters
def introduce(name, age):
    return f"I am {name}, {age} years old"

print(introduce("Alice", 25))

# Example 5: Default return (None)
def greet(name):
    return f"Hello, {name}!"

def no_return():
    print("I don't return anything")

result = no_return()
print(result)  # None
```

## Best Practices

```python
# ✅ Good: Clear names
def calculate_area(width, height):
    return width * height

# ✅ Good: Docstrings
def calculate_area(width, height):
    """Calculate the area of a rectangle."""
    return width * height

# ⚠️ Bad: Magic numbers
# Don't do this
def get_price():
    return 100 * 1.5  # What is 1.5?
```

## Key Takeaways

1. **def** keyword defines functions
2. **Parameters** are inputs in parentheses
3. **return** sends back a value
4. **None** is returned if no return statement
5. **Call** with function_name()

## Practice Exercise

1. Create a function that prints "Hello World"
2. Create a function that takes a name and prints a greeting
3. Create a function that adds two numbers and returns the result
4. Call all functions