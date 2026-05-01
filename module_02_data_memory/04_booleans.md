# The Primitive Types: Booleans (True/False Logic)

## Learning Objectives

By the end of this lesson, you will be able to:

- Understand the boolean data type and its two possible values
- Create booleans from comparisons
- Use booleans to make decisions in your code

---

## Mental Model: Light Switch

A boolean is the simplest data type in Python — it can only be one of two things:

```
True   ← Light switch is ON
False  ← Light switch is OFF
```

That's it. Every decision in every program ultimately comes down to `True` or `False`.

---

## Creating Booleans

### Direct Assignment

```python
is_raining = True
is_sunny = False
```

### From Comparisons

Most booleans come from comparisons:

```python
print(10 > 5)      # True
print(10 < 5)      # False
print(10 == 10)    # True (equals)
print(10 != 5)     # True (not equals)
print("a" == "A")  # False (case-sensitive)
```

---

## Capitalization Matters

```python
# ✅ Correct — Python keywords are case-sensitive
is_valid = True
is_active = False

# ❌ Wrong — lowercase 'true' is not recognized
is_valid = true    # NameError: name 'true' is not defined
is_active = false  # NameError: name 'false' is not defined
```

Python's booleans are **capitalized**: `True` and `False`. Always.

---

## The "Truthy" and "Falsy" Concept

In Python, many values behave like booleans:

| Falsy (behaves like `False`) | Truthy (behaves like `True`) |
|------------------------------|------------------------------|
| `False` | `True` |
| `0` | `1`, `42`, any non-zero number |
| `""` (empty string) | `"hello"`, any non-empty string |
| `[]` (empty list) | `[1, 2, 3]`, any non-empty list |
| `None` | Almost anything else |

```python
# These all evaluate to False in conditions
print(bool(0))       # False
print(bool(""))      # False
print(bool([]))      # False
print(bool(None))    # False

# These all evaluate to True
print(bool(1))       # True
print(bool("hello")) # True
print(bool([1, 2]))  # True
```

---

## Common Mistakes

```
❌ Using lowercase true/false
   is_valid = true    → NameError
   is_valid = True    ← Correct

❌ Confusing == with =
   if x = 5:         → SyntaxError (use == for comparison)
   if x == 5:        ← Correct

❌ Comparing booleans to True/False
   if is_raining == True:   ← Works, but not Pythonic
   if is_raining:           ← Clean and Pythonic

❌ Assuming float comparison is exact
   0.1 + 0.2 == 0.3  → False (floating-point issue, not a boolean issue)
```

---

## Code Examples

### Example 1 — Basic Boolean

```python
is_raining = True
print(f"Is it raining? {is_raining}")  # Is it raining? True
```

### Example 2 — Boolean from Comparison

```python
age = 18
is_adult = age >= 18
print(f"Is adult: {is_adult}")  # True
```

### Example 3 — Boolean Operators

```python
is_sunny = True
is_warm = False

# AND — both must be True
print(is_sunny and is_warm)   # False

# OR — at least one must be True
print(is_sunny or is_warm)    # True

# NOT — inverts the value
print(not is_sunny)           # False
```

### Example 4 — Combining Conditions

```python
age = 25
has_license = True

# Can drive if both conditions are True
can_drive = age >= 18 and has_license
print(f"Can drive: {can_drive}")  # True
```

### Example 5 — Boolean from String Operations

```python
email = "user@example.com"

# Check if email contains "@"
is_valid_email = "@" in email
print(f"Valid email: {is_valid_email}")  # True

# Check if name is empty
name = ""
is_empty = not name
print(f"Name is empty: {is_empty}")  # True
```

### Example 6 — Truthy and Falsy

```python
# Check truthiness
print(bool(0))        # False
print(bool(1))        # True
print(bool(-1))       # True (any non-zero is True)
print(bool(""))       # False
print(bool("hello"))  # True
```

---

## Practice Exercise

1. Create two boolean variables:
   - `has_python_book` (True or False)
   - `has_experience` (True or False)
2. Print whether you have both
3. Print whether you have at least one
4. Print the opposite of `has_experience`

---

## Key Takeaways

- **Booleans have only two values**: `True` and `False`
- **Capitalization matters**: `True`, not `true`
- **Comparisons return booleans**: `10 > 5` → `True`
- **Truthy/Falsy**: Many values behave like booleans in conditions
- **Keep it simple**: `if is_raining:` is cleaner than `if is_raining == True:`

---

## Further Reading

- [Boolean Operations — Official Docs](https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not)
- [Truth Value Testing — Official Docs](https://docs.python.org/3/library/stdtypes.html#truth-value-testing)
- [Python Comparison Operators — Real Python](https://realpython.com/python-operators-expressions/)