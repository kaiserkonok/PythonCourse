# Code examples from "Error & Exception Handling" lesson

# Example 1: Basic try/except
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

print("---")

# Example 2: Multiple exceptions
try:
    value = int("hello")
except ValueError:
    print("Invalid value")
except TypeError:
    print("Wrong type")

print("---")

# Example 3: Catch all exceptions
try:
    result = 10 / 0
except Exception as e:
    print(f"Error: {e}")

print("---")

# Example 4: Try/except/else
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print(f"Result: {result}")  # Runs if no error

print("---")

# Example 5: Try/except/finally (always runs)
try:
    x = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("Cleanup complete")  # Always runs


# =====================
# PRACTICE EXERCISE
# =====================

# 1. Handle division by zero
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"

print(safe_divide(10, 2))
print(safe_divide(10, 0))

# 2. Handle invalid input conversion
def safe_convert(value):
    try:
        return int(value)
    except ValueError:
        return "Invalid input"

print(safe_convert("42"))
print(safe_convert("hello"))

# 3. Use try/except/finally
def read_number(value):
    try:
        return int(value)
    except ValueError:
        return 0
    finally:
        print("Conversion attempted")

print(read_number("100"))
print(read_number("abc"))

# 4. Create a custom exception
class InvalidAgeError(Exception):
    pass

def validate_age(age):
    if age < 0:
        raise InvalidAgeError("Age cannot be negative!")
    if age > 150:
        raise InvalidAgeError("Age seems invalid!")
    return age

try:
    validate_age(-5)
except InvalidAgeError as e:
    print(f"Error: {e}")

try:
    validate_age(200)
except InvalidAgeError as e:
    print(f"Error: {e}")