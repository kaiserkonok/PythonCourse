# Code examples from "Namespace & Scope" lesson

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


# =====================
# PRACTICE EXERCISE
# =====================

# 1. Create a global variable
global_var = "I am global"

# 2. Create a function that reads it
def read_global():
    print(f"Reading: {global_var}")

read_global()

# 3. Create a function that tries to modify it (before global)
def try_modify():
    print(f"Before global: {global_var}")  # Can read
    # global_var = "Modified locally"  # This creates a local variable!
    # print(try_modify_local())  # Would show local

# 4. Use global to actually modify it
def modify_with_global():
    global global_var
    global_var = "Modified by function!"

modify_with_global()
print(f"Now global_var is: {global_var}")