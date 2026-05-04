"""
Defining Functions (Reusable Code Blocks)
────────────────────────────────────────────────────────────────────────────
Code examples and practice exercises from the lesson.
────────────────────────────────────────────────────────────────────────────
"""

# Example 1 — Simple Function
def greet():
    """Prints a greeting message."""
    print("Hello, World!")

greet()  # Call the function


# Example 2 — Function with Parameters
def greet(name):
    """Greets a specific person."""
    print(f"Hello, {name}!")

greet("Alice")  # Hello, Alice!
greet("Bob")    # Hello, Bob!


# Example 3 — Returning Values
def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

result = add(5, 3)
print(f"Sum: {result}")  # Sum: 8


# Example 4 — Multiple Returns
def get_stats(numbers):
    """Returns min, max, and average."""
    return min(numbers), max(numbers), sum(numbers) / len(numbers)

low, high, avg = get_stats([10, 20, 30, 40])
print(f"Low: {low}, High: {high}, Avg: {avg}")


# Example 5 — No Return (Implicit None)
def log_message(msg):
    """Just prints, doesn't return anything."""
    print(f"LOG: {msg}")

result = log_message("Starting...")
print(f"Returned: {result}")  # Returned: None


# Example 6 — Function as Variable
def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

# Assign function to variable
speak = shout
print(speak("Hello"))  # HELLO

# Pass function as argument
def process(text, func):
    return func(text)

print(process("Hello", whisper))  # hello


# ═══════════════════════════════════════════════════════════════════════════════
# PRACTICE EXERCISE
# ═══════════════════════════════════════════════════════════════════════════════
# 1. Define a function that takes a name and returns a greeting
# 2. Create a function that calculates the area of a circle
# 3. Write a function that returns multiple values (e.g., square and cube)
# 4. Create a function that prints a pattern
# ═══════════════════════════════════════════════════════════════════════════════

# 1. Greeting
def make_greeting(name):
    return f"Hello, {name}!"

print(make_greeting("Charlie"))

# 2. Circle area
import math
def circle_area(radius):
    return math.pi * radius ** 2

print(f"Area: {circle_area(5)}")

# 3. Multiple returns
def powers(n):
    return n**2, n**3

sq, cb = powers(4)
print(f"Square: {sq}, Cube: {cb}")

# 4. Pattern
def print_triangle(height):
    for i in range(1, height + 1):
        print("*" * i)

print_triangle(5)

# Try modifying it:
# - Create a function that validates an email address
def is_valid_email(email):
    return "@" in email and "." in email

print(f"Valid: {is_valid_email('test@example.com')}")
