# Logical Operators: Building Complex Conditions

## Learning Objectives

- Combine conditions with `and`, `or`, and `not`
- Understand truth tables
- Use logical operators in real code

## The Three Logical Operators

| Operator | Description | Returns True when |
|----------|-------------|-------------------|
| and | Both must be True | All conditions are True |
| or | At least one must be True | Any condition is True |
| not | Inverts the condition | Condition is False |

## Using and, or, not

```python
# AND - Both conditions must be True
age = 25
has_license = True
can_drive = age >= 18 and has_license
print(can_drive)  # True (both are True)
```

```python
# OR - At least one condition must be True
has_card = False
has_cash = True
can_buy = has_card or has_cash
print(can_buy)  # True (has_cash is True)
```

```python
# NOT - Inverts the boolean
is_raining = True
is_outdoor = not is_raining
print(is_outdoor)  # False
```

## The Truth Table

### AND

| A | B | A and B |
|---|---|---------|
| True | True | True |
| True | False | False |
| False | True | False |
| False | False | False |

### OR

| A | B | A or B |
|---|---|---------|
| True | True | True |
| True | False | True |
| False | True | True |
| False | False | False |

### NOT

| A | not A |
|---|-------|
| True | False |
| False | True |

## Real-World Examples

```python
# Example 1: Login validation
username = "alice"
password = "secret123"
is_valid_user = username == "alice"
is_valid_pass = password == "secret123"
can_login = is_valid_user and is_valid_pass
print(f"Can login: {can_login}")
```

```python
# Example 2: Multiple conditions
age = 16
has_permission = False
is_adult = age >= 18
can_access = is_adult or has_permission
print(f"Can access: {can_access}")  # False
```

## Combining Multiple Operators

```python
# Mix and, or with parentheses
age = 25
is_student = False
has_id = True

# Complex condition
can_enter = (age >= 18 or is_student) and has_id
print(can_enter)  # True
```

## Code Examples

```python
# Example 1: Basic and
is_sunny = True
is_warm = True
is_good_weather = is_sunny and is_warm
print(f"Good weather: {is_good_weather}")  # True

# Example 2: Basic or
is_weekend = False
is_holiday = True
can_rest = is_weekend or is_holiday
print(f"Can rest: {can_rest}")  # True

# Example 3: Not
is_raining = False
print(not is_raining)  # True

# Example 4: Complex condition
age = 16
has_parent = True
can_watch_movie = age >= 17 or has_parent
print(f"Can watch: {can_watch_movie}")  # True

# Example 5: Short-circuit evaluation
# Python stops evaluating as soon as it knows the result
x = 5
result = x > 10 and x / 0  # Won't divide by 0!
print(result)  # False (stops at first condition)
```

## Key Takeaways

1. **and** - Both conditions must be True
2. **or** - At least one must be True
3. **not** - Inverts the boolean
4. **Short-circuit** - Python stops early if result is determined
5. **Use parentheses** to group conditions clearly

## Practice Exercise

1. Create two booleans: is_student (True), has_id (True)
2. Use and to check both conditions
3. Use or to check at least one condition
4. Use not to invert is_student
5. Create a complex condition with and, or, not