# The Primitive Types: Booleans (True/False Logic)

## Learning Objectives

- Understand the boolean data type
- Learn True and False values
- Use booleans in conditional logic

## What is a Boolean?

A boolean represents **truth values** - either True or False.

- Only two possible values: True or False
- Used for making decisions in code
- Foundation of all programming logic

```python
is_active = True
is_admin = False
```

## Boolean in Everyday Programming

```python
# Is user logged in?
is_logged_in = True

# Is user an admin?
is_admin = False

# Is account active?
is_active = True
```

## Boolean from Comparisons

Many operations return booleans:

```python
# Comparison operators return True or False
print(10 > 5)      # True
print(10 < 5)      # False
print(10 == 10)    # True (equals)
print(10 != 5)     # True (not equals)

# Check string equality
name = "Alice"
print(name == "Alice")   # True
print(name == "Bob")      # False
```

## Boolean Values in Python

| Expression | Result |
|-------------|-------|
| True | True |
| False | False |
| 1 == 1 | True |
| 1 == 2 | False |
| "Python" == "python" | False (case-sensitive) |

```python
# Be careful with capitalization!
is_valid = true    # ❌ NameError: name 'true' is not defined
is_valid = True    # ✅ Correct

is_active = false   # ❌ NameError
is_active = False   # ✅ Correct
```

## Using Booleans

```python
# Simple boolean variable
is_student = True
print(f"Is student: {is_student}")

# Boolean from comparison
age = 18
is_adult = age >= 18
print(f"Is adult: {is_adult}")  # True

# Boolean in if statements (more in Module 4)
if is_adult:
    print("You can vote!")
```

## Code Examples

```python
# Example 1: Basic boolean
is_raining = True
print(f"Is it raining? {is_raining}")

# Example 2: Boolean operators
is_sunny = True
is_warm = False
print(is_sunny and is_warm)   # False (both must be True)
print(is_sunny or is_warm)    # True (at least one is True)
print(not is_sunny)          # False (opposite)

# Example 3: Comparison to boolean
score = 85
passed = score >= 60
print(f"Passed: {passed}")  # True

# Example 4: Multiple comparisons
age = 25
has_license = True
can_drive = age >= 18 and has_license
print(f"Can drive: {can_drive}")  # True

# Example 5: Boolean from string methods
email = "user@example.com"
is_valid = "@" in email
print(f"Valid email: {is_valid}")  # True
```

## Key Takeaways

1. **Booleans** have only two values: True or False
2. **Capitalization matters**: True, not true
3. **Comparisons** return boolean values
4. **Boolean operators**: and, or, not
5. **Used in decisions** - the foundation of program flow

## Practice Exercise

1. Create two boolean variables:
   - has_python_book (True or False)
   - has_experience (True or False)
2. Print whether you have both
3. Print whether you have at least one
4. Print the opposite of has_experience