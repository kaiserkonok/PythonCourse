# Namespace & Scope: Global vs Local Variables

## Learning Objectives

- Understand global and local scope
- Use the global keyword
- Avoid scope confusion

## What is Scope?

Scope determines **where variables are accessible**:

- **Local** - Inside a function
- **Global** - Everywhere in the file

```python
# Global variable
global_var = 10

def my_function():
    # Local variable
    local_var = 20
    print(local_var)  # Works here
    print(global_var)  # Works here

print(global_var)  # Works
# print(local_var)  # ERROR! Not accessible here
```

## Local vs Global

```python
x = 10  # Global

def my_function():
    x = 20  # Local (different variable!)
    print(x)     # 20 (local)

my_function()
print(x)         # 10 (global unchanged)
```

## The Global Keyword

To modify a global variable from inside a function:

```python
x = 10

def update_global():
    global x  # Tell Python to use global x
    x = 20

update_global()
print(x)  # 20 (updated!)
```

## Code Examples

```python
# Example 1: Local scope
def greet():
    message = "Hello!"  # Local
    print(message)

greet()  # Hello!
# print(message)  # ERROR!

# Example 2: Global scope
message = "World"

def say_hello():
    print(f"Hello, {message}!")

say_hello()  # Hello, World!

# Example 3: Same name, different scopes
name = "Alice"  # Global

def greet():
    name = "Bob"  # Local (different!)
    print(f"Hello, {name}!")  # Bob

greet()
print(name)  # Alice (unchaged)

# Example 4: Global keyword
counter = 0

def increment():
    global counter
    counter += 1

increment()
print(counter)  # 1
increment()
print(counter)  # 2

# Example 5: Nested functions
def outer():
    x = "outer"
    
    def inner():
        nonlocal x  # Refers to outer's x
        x = "modified"
        print(f"Inner: {x}")
    
    inner()
    print(f"Outer: {x}")

outer()
```

## Best Practices

- **Avoid global variables** - Pass values as parameters
- **Use return** - Send values back instead of modifying globals
- **Minimize scope** - Keep variables as local as possible

## Key Takeaways

1. **Local** - Only accessible inside function
2. **Global** - Accessible everywhere
3. **Same name** = different variables
4. **global** keyword modifies global
5. **Avoid globals** when possible

## Practice Exercise

1. Create a global variable
2. Create a function that reads it
3. Create a function that tries to modify it (before global)
4. Use global to actually modify it