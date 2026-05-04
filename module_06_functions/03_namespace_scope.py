"""
Namespace & Scope (Where Variables Live)
────────────────────────────────────────────────────────────────────────────
Code examples and practice exercises from the lesson.
────────────────────────────────────────────────────────────────────────────
"""

# Example 1 — Local Scope
def greet():
    message = "Hello!"  # Local variable
    print(message)

greet()
# print(message)  → NameError (not visible outside)


# Example 2 — Global Scope
name = "World"  # Global

def greet_global():
    print(f"Hello, {name}!")  # Can read globals

greet_global()  # Hello, World!


# Example 3 — Shadowing
x = 100  # Global

def shadow():
    x = 50  # Local (shadows global)
    print(f"Local: {x}")

shadow()      # Local: 50
print(f"Global: {x}")  # Global: 100


# Example 4 — The `global` Keyword
score = 0

def add_points(pts):
    global score
    score += pts

add_points(10)
add_points(5)
print(f"Score: {score}")  # Score: 15


# Example 5 — Nested Functions
def outer():
    x = "outer"

    def inner():
        x = "inner"
        print(x)  # inner (local)

    inner()
    print(x)  # outer (enclosing)

outer()


# Example 6 — Closures
def make_multiplier(factor):
    def multiply(x):
        return x * factor
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))  # 10
print(triple(5))  # 15


# ═══════════════════════════════════════════════════════════════════════════════
# PRACTICE EXERCISE
# ═══════════════════════════════════════════════════════════════════════════════
# 1. Create a function that uses a local variable
# 2. Try to access a local variable from outside and see the error
# 3. Use global to modify a global counter
# 4. Create a closure that remembers a value
# ═══════════════════════════════════════════════════════════════════════════════

# 1. Local variable
def local_demo():
    secret = "I'm local!"
    print(secret)

local_demo()

# 2. Accessing local outside (commented out to avoid crash)
# print(secret)  → NameError

# 3. Global counter
call_count = 0

def track_calls():
    global call_count
    call_count += 1
    print(f"Called {call_count} times")

track_calls()
track_calls()

# 4. Closure
def power_of(n):
    def calculate(x):
        return x ** n
    return calculate

square = power_of(2)
cube = power_of(3)
print(f"4 squared: {square(4)}, 4 cubed: {cube(4)}")

# Try modifying it:
# - Use nonlocal to modify a variable in an outer (non-global) scope
def counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

c = counter()
print(c())  # 1
print(c())  # 2
print(c())  # 3
