"""
Error Handling (Graceful Failures)
────────────────────────────────────────────────────────────────────────────
Code examples and practice exercises from the lesson.
────────────────────────────────────────────────────────────────────────────
"""

# Example 1 — Basic Try/Except
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Can't divide by zero!")


# Example 2 — Multiple Exceptions
try:
    value = int("hello")
except ValueError:
    print("Invalid number!")
except TypeError:
    print("Wrong type!")


# Example 3 — Else and Finally
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Error!")
else:
    print(f"Result: {result}")  # Runs if no error
finally:
    print("Cleanup done")       # Always runs


# Example 4 — Catching Multiple Types
def safe_divide(a, b):
    try:
        return a / b
    except (ZeroDivisionError, TypeError) as e:
        print(f"Error: {e}")
        return None

print(safe_divide(10, 2))   # 5.0
print(safe_divide(10, 0))   # Error + None
print(safe_divide(10, "2")) # Error + None


# Example 5 — Raising Exceptions
def set_age(age):
    if age < 0:
        raise ValueError("Age can't be negative")
    if age > 150:
        raise ValueError("Age seems unrealistic")
    return age

try:
    set_age(-5)
except ValueError as e:
    print(f"Invalid: {e}")


# Example 6 — Custom Exceptions
class InsufficientFundsError(Exception):
    """Custom exception for bank accounts."""
    pass

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(
                f"Need ${amount - self.balance} more"
            )
        self.balance -= amount

acc = BankAccount(100)
try:
    acc.withdraw(150)
except InsufficientFundsError as e:
    print(f"Failed: {e}")


# ═══════════════════════════════════════════════════════════════════════════════
# PRACTICE EXERCISE
# ═══════════════════════════════════════════════════════════════════════════════
# 1. Write a function that safely converts user input to an integer
# 2. Handle multiple exception types in one block
# 3. Use finally to ensure cleanup happens
# 4. Create a custom exception and raise it
# ═══════════════════════════════════════════════════════════════════════════════

# 1. Safe integer conversion
def safe_int(value):
    try:
        return int(value)
    except ValueError:
        print(f"Can't convert '{value}' to int")
        return None

print(safe_int("42"))    # 42
print(safe_int("hello")) # Error + None

# 2. Multiple exceptions
def process(data):
    try:
        result = int(data) * 2
        print(f"Result: {result}")
    except ValueError:
        print("Not a valid number")
    except TypeError:
        print("Wrong type")
    finally:
        print("Processing complete")

process("10")
process("abc")

# 3. Finally for cleanup
file_data = None
try:
    # Simulated file operation
    file_data = "Some data"
    print("File opened")
except Exception:
    print("Error reading file")
finally:
    if file_data:
        print("File closed")

# 4. Custom exception
class NegativeRadiusError(Exception):
    pass

def circle_area(radius):
    if radius < 0:
        raise NegativeRadiusError("Radius cannot be negative")
    return 3.14 * radius ** 2

try:
    circle_area(-5)
except NegativeRadiusError as e:
    print(f"Error: {e}")

# Try modifying it:
# - Create a context manager for resource management
class SafeResource:
    def __enter__(self):
        print("Resource acquired")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Resource released")
        return False  # Don't suppress exceptions

with SafeResource():
    print("Using resource")
