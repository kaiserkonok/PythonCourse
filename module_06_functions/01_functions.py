# Code examples from "Defining Functions" lesson

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


# =====================
# PRACTICE EXERCISE
# =====================

# 1. Create a function that prints "Hello World"
def hello_world():
    print("Hello World")

hello_world()

# 2. Create a function that takes a name and prints a greeting
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Alice")
greet_person("Bob")

# 3. Create a function that adds two numbers and returns the result
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)
print(f"5 + 3 = {result}")

# 4. Call all functions
def calculate_square(x):
    return x * x

print(f"5 squared = {calculate_square(5)}")