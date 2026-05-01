# Decorators: Functions That Wrap Other Functions

## Learning Objectives

- Understand what decorators are
- Create basic decorators
- Use @decorator syntax

## What is a Decorator?

A decorator **adds behavior** to a function without modifying it:

```python
def my_decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
```

## Creating Decorators

```python
def timer_decorator(func):
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Took {end - start} seconds")
        return result
    return wrapper

@timer_decorator
def slow_function():
    import time
    time.sleep(1)
    print("Done!")

slow_function()  # Takes ~1 second
```

## Passing Arguments to Decorators

```python
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet():
    print("Hello!")

greet()  # Prints "Hello!" 3 times
```

## Code Examples

```python
# Example 1: Basic decorator
def uppercase_decorator(func):
    def wrapper():
        return func().upper()
    return wrapper

@uppercase_decorator
def sayhello():
    return "hello"

print(sayhello())  # HELLO

# Example 2: Decorator with arguments
def repeat(times):
    def decorator(func):
        def wrapper():
            for _ in range(times):
                func()
        return wrapper
    return decorator

@repeat(3)
def message():
    print("Hi!")

message()  # Prints "Hi!" 3 times

# Example 3: Preserve function metadata
import functools

def logged(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Called {func.__name__}")
        return result
    return wrapper

@logged
def add(a, b):
    return a + b

print(add(1, 2))

# Example 4: Timing decorator
def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Took {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def slow():
    import time
    time.sleep(0.1)

slow()

# Example 5: Authentication decorator
def requires_auth(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        user_logged_in = False  # Change to test
        
        if not user_logged_in:
            return "Please login first!"
        
        return func(*args, **kwargs)
    return wrapper

@requires_auth
def secret_data():
    return "Secret info!"

print(secret_data())  # Please login first!
```

## Common Uses

- **Logging** - track function calls
- **Timing** - measure performance
- **Authentication** - check permissions
- **Caching** - store results
- **Validation** - check inputs

## Key Takeaways

1. **Decorator** takes function, returns new function
2. **@decorator** syntax applies it
3. ** functools.wraps** preserves metadata
4. **Arguments** need extra wrapper layer
5. **Used for** - cross-cutting concerns

## Practice Exercise

1. Create a decorator that prints before/after
2. Create a decorator with argument
3. Use functools.wraps properly
4. Create an authentication decorator