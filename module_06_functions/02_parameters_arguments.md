# Parameters & Arguments: Positional, Keyword, and Default

## Learning Objectives

- Use positional arguments
- Use keyword arguments
- Set default parameter values

## Types of Arguments

| Type | Example | Description |
|------|---------|-------------|
| Positional | func(a, b) | By position |
| Keyword | func(a=1, b=2) | By name |
| Default | func(a=1) | Uses default if not provided |

## Positional Arguments

```python
def greet(first_name, last_name):
    return f"Hello, {first_name} {last_name}!"

# Call with positional arguments
print(greet("Alice", "Smith"))
```

## Keyword Arguments

```python
def greet(first_name, last_name):
    return f"Hello, {first_name} {last_name}!"

# Call with keyword arguments
print(greet(last_name="Smith", first_name="Alice"))
```

## Default Values

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Alice"))           # Hello, Alice!
print(greet("Alice", "Hi"))    # Hi, Alice!
```

## Code Examples

```python
# Example 1: Positional arguments
def add(a, b, c):
    return a + b + c

print(add(1, 2, 3))  # 6

# Example 2: Keyword arguments
def create_user(name, age, city):
    return f"{name}, {age}, {city}"

# Order doesn't matter with keywords
print(create_user(city="NYC", name="Alice", age=25))
print(create_user(name="Bob", city="LA", age=30))

# Example 3: Default parameters
def power(base, exponent=2):
    return base ** exponent

print(power(3))     # 9 (exponent defaults to 2)
print(power(3, 3))  # 27

# Example 4: Combining positional and keyword
def describe(name, age, role="user"):
    return f"{name} is {age} years old, role: {role}"

print(describe("Alice", 25))                  # role is "user"
print(describe("Bob", 30, role="admin"))      # role is "admin"
print(describe(age=35, name="Charlie"))       # mixed

# Example 5: *args and **kwargs (later)
def print_all(*args, **kwargs):
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")

print_all(1, 2, 3, name="Alice", age=25)
```

## Common Mistakes

```python
# ❌ Wrong: Non-default after default
def func(a=1, b):  # SyntaxError!
    pass

# ✅ Correct: Defaults at the end
def func(a, b=1):
    pass
```

## Key Takeaways

1. **Positional** - order matters
2. **Keyword** - name=value
3. **Default** - uses value if not provided
4. **Order**: positional first, then keyword
5. **Defaults** must come after positional parameters

## Practice Exercise

1. Create a function with 3 parameters, one with default
2. Call with positional arguments only
3. Call with keyword arguments only
4. Mix both types