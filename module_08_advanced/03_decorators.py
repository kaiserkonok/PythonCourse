# Code examples from "Decorators" lesson

# Example 1: Basic decorator
def uppercase_decorator(func):
    def wrapper():
        return func().upper()
    return wrapper

@uppercase_decorator
def sayhello():
    return "hello"

print(sayhello())  # HELLO

print("---")

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

print("---")

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

print(f"Result: {add(1, 2)}")

print("---")

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

print("---")

# Example 5: Authentication decorator
def requires_auth(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        user_logged_in = True  # Change to test
        
        if not user_logged_in:
            return "Please login first!"
        
        return func(*args, **kwargs)
    return wrapper

@requires_auth
def secret_data():
    return "Secret info!"

print(secret_data())