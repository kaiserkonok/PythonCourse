# 🛡️ Error Handling: Graceful Failures

<p align="center">
  <img src="https://img.shields.io/badge/try-Catch%20Errors-blue?style=flat-square" alt="try">
  <img src="https://img.shields.io/badge/except-Handle-green?style=flat-square" alt="except">
  <img src="https://img.shields.io/badge/finally-Cleanup-orange?style=flat-square" alt="finally">
</p>

> ### 💡 Error handling is like a safety net — your program might trip, but it won't crash. Learn how to catch and handle problems gracefully.
> Master try/except/else/finally for robust code.

---

## 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- ✅ Use `try/except` to catch and handle errors
- ✅ Catch specific exception types
- ✅ Use `else` and `finally` blocks
- ✅ Raise custom exceptions

---

## 🧠 Mental Model: A Safety Net

Error handling is like a **trapeze artist's safety net**:

```
🎪 Try (Perform the act)
   └── 🛡️ Except (Catch if they fall)
   └── ✅ Else (Celebrate if they succeed)
   └── 🔧 Finally (Clean up regardless)
```

---

## 📖 Basic Syntax

```python
try:
    # Code that might fail
    risky_operation()
except SomeError:
    # Handle the error
    print("Something went wrong!")
else:
    # Runs if NO error occurred
    print("Success!")
finally:
    # Always runs (cleanup)
    print("Done")
```

---

## 📊 Common Exceptions

| Exception | When it happens | Example |
|-----------|----------------|---------|
| `ValueError` | Wrong value type | `int("hello")` |
| `TypeError` | Wrong type operation | `"2" + 2` |
| `KeyError` | Missing dict key | `d["missing"]` |
| `IndexError` | Invalid index | `lst[999]` |
| `FileNotFoundError` | File doesn't exist | `open("no.txt")` |
| `ZeroDivisionError` | Divide by zero | `10 / 0` |

---

## ⚠️ Common Mistakes

```
❌ Bare except (catches everything)
   except:  ← Catches ALL errors, including KeyboardInterrupt!
   except Exception:  ← Better but still broad
   except ValueError:  ← Best — specific

❌ Hiding errors
   try:
       do_something()
   except:
       pass  ← Silently ignores errors!

❌ Too broad try block
   try:
       read_file()
       process_data()
       save_result()
   except:  ← Which operation failed?
   ← Wrap only the risky operation

❌ Not using finally for cleanup
   f = open("file.txt")
   try:
       process(f)
   except:
       handle()
   f.close()  ← Might not run if exception before!
```

---

## 💻 Code Examples

### 📌 Example 1 — Basic Try/Except

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Can't divide by zero!")
```

### 📌 Example 2 — Multiple Exceptions

```python
try:
    value = int("hello")
except ValueError:
    print("Invalid number!")
except TypeError:
    print("Wrong type!")
```

### 📌 Example 3 — Else and Finally

```python
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Error!")
else:
    print(f"Result: {result}")  # Runs if no error
finally:
    print("Cleanup done")       # Always runs
```

### 📌 Example 4 — Catching Multiple Types

```python
def safe_divide(a, b):
    try:
        return a / b
    except (ZeroDivisionError, TypeError) as e:
        print(f"Error: {e}")
        return None

print(safe_divide(10, 2))   # 5.0
print(safe_divide(10, 0))   # Error + None
print(safe_divide(10, "2")) # Error + None
```

### 📌 Example 5 — Raising Exceptions

```python
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
```

### 📌 Example 6 — Custom Exceptions

```python
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
```

---

## 🧪 Practice Exercise

1. Write a function that safely converts user input to an integer
2. Handle multiple exception types in one block
3. Use finally to ensure cleanup happens
4. Create a custom exception and raise it

---

## 📋 Key Takeaways

| Concept | Takeaway |
|---------|----------|
| 🛡️ **try/except** | Catch and handle errors |
| 🔍 **Specific** | Catch specific exceptions, not bare `except` |
| ✅ **else** | Runs only if no error occurred |
| 🔧 **finally** | Always runs — use for cleanup |
| 🚀 **raise** | Throw your own exceptions |

---

## 🔗 Further Reading

- 📖 [Errors and Exceptions — Official Docs](https://docs.python.org/3/tutorial/errors.html)
- 🌟 [Exception Handling — Real Python](https://realpython.com/python-exceptions/)
- 🔧 [Built-in Exceptions — docs](https://docs.python.org/3/library/exceptions.html)