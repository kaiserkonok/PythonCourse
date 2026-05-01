# Code examples from "Parameters & Arguments" lesson

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

# Example 5: *args and **kwargs
def print_all(*args, **kwargs):
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")

print_all(1, 2, 3, name="Alice", age=25)


# =====================
# PRACTICE EXERCISE
# =====================

# 1. Create a function with 3 parameters, one with default
def create_profile(name, age, city="Unknown"):
    return f"{name}, {age}, {city}"

# 2. Call with positional arguments only
print(create_profile("Alice", 25, "NYC"))

# 3. Call with keyword arguments only
print(create_profile(name="Bob", age=30, city="LA"))

# 4. Mix both types
print(create_profile("Charlie", city="Tokyo", age=35))