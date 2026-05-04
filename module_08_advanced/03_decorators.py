"""
Decorators (Enhancing Functions)
────────────────────────────────────────────────────────────────────────────
Code examples and practice exercises from the lesson.
────────────────────────────────────────────────────────────────────────────
"""

# Example 1 — Simple Decorator
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


# Example 2 — Decorator with Arguments
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


# Example 3 — Timing Decorator
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


# Example 4 — Logging Decorator
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


# Example 5 — Preserving Metadata
from functools import wraps

def my_decorator_wraps(func):
    @wraps(func)  # Preserves name and docstring
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@my_decorator_wraps
def greet_doc(name):
    """Greets a person."""
    print(f"Hi, {name}!")

print(greet_doc.__name__)  # greet_doc (not wrapper!)
print(greet_doc.__doc__)   # Greets a person.


# Example 6 — Class Decorator
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


# ═══════════════════════════════════════════════════════════════════════════════
# PRACTICE EXERCISE
# ═══════════════════════════════════════════════════════════════════════════════
# 1. Create a decorator that prints "Starting" and "Finished" around any function
# 2. Create a decorator that retries a function if it fails
# 3. Use @wraps to preserve function metadata
# 4. Create a decorator that caches function results
# ═══════════════════════════════════════════════════════════════════════════════

# 1. Starting/Finished decorator
def boundary(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Starting...")
        result = func(*args, **kwargs)
        print("Finished!")
        return result
    return wrapper

@boundary
def process():
    print("Processing...")

process()

# 2. Retry decorator
def retry(times=3):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempt + 1} failed: {e}")
            raise Exception("All attempts failed")
        return wrapper
    return decorator

@retry(2)
def risky():
    import random
    if random.random() < 0.7:
        raise ValueError("Bad luck!")
    return "Success!"

try:
    print(risky())
except Exception as e:
    print(e)

# 3. @wraps already shown above

# 4. Cache decorator
def cache(func):
    cache_data = {}
    @wraps(func)
    def wrapper(*args):
        if args in cache_data:
            print(f"Cache hit for {args}")
            return cache_data[args]
        result = func(*args)
        cache_data[args] = result
        return result
    return wrapper

@cache
def expensive(n):
    print(f"Computing {n}...")
    return n ** 2

print(expensive(4))
print(expensive(4))  # Cache hit!
print(expensive(5))

# Try modifying it:
# - Decorator that checks if user is authorized
def requires_auth(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if kwargs.get("authorized"):
            return func(*args, **kwargs)
        return "Access denied!"
    return wrapper

@requires_auth
def admin_panel(user, authorized=False):
    return f"Welcome, {user}!"

print(admin_panel("Alice", authorized=True))
print(admin_panel("Bob", authorized=False))
