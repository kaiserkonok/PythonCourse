# Variables & Memory Labels: How Data is Stored and Referenced

## Learning Objectives

- Understand what variables are and how they work
- Learn how data is stored in RAM (memory)
- Create and use variables effectively

## What is a Variable?

A variable is a **named container** that stores data in memory.

Think of it like a labeled box:
```
┌─────────────┐
│    Box      │
│  ┌────────┐ │
│  │   42   │ │
│  └────────┘ │
│   label: x  │
└─────────────┘
```

- The **box** holds the data
- The **label** is the variable name
- The **data** is the value (42)

## How Variables Work in Memory

```python
x = 10
```

1. Python allocates space in RAM
2. Stores the value (10)
3. Creates a label (x) that points to that memory location

```
RAM:
┌──────────┬──────────┬──────────┬──────────┐
│ Address  │  ...     │ x → 10   │          │
│ 0x001    │          │          │          │
└──────────┴──────────┴──────────┴──────────┘
```

## Variable Naming Rules

| Rule | Correct | Incorrect |
|------|---------|-----------|
| Start with letter or _ | name, _value | 2name |
| Letters, numbers, _ only | user_name | user-name |
| Case-sensitive | Age, age, AGE | are all different |
| No spaces | my_value | my value |
| Can't use keywords | score | if, for, while |

## Valid Variable Names

```python
# Good variable names
name = "Alice"
age = 25
user_name = "alice123"
_score = 100
firstName = "Alice"  # camelCase (less Pythonic)
FirstName = "Alice"  # PascalCase (less Pythonic)

# Pythonic convention: snake_case
user_name = "alice"
current_balance = 1000
is_active = True
```

## Code Examples

```python
# Example 1: Create a variable
player_name = "Mario"
print(player_name)

# Example 2: Reassign a variable
age = 25
print(age)
age = 26  # Overwrites the old value
print(age)

# Example 3: Multiple variables
x = 5
y = 10
z = x + y
print(z)  # Output: 15

# Example 4: Swap values
a = 1
b = 2
a, b = b, a  # Pythonic swap
print(f"a = {a}, b = {b}")  # a = 2, b = 1
```

## Key Takeaways

1. **Variables store data** - they're like labeled boxes
2. **The assignment operator (=)** assigns value to variable
3. **Variables are references** - they point to memory locations
4. **Reassigning overwrites** the old value
5. **Pythonic naming:** snake_case (user_name, not userName)

## Practice Exercise

Create variables for:
1. Your first name
2. Your last name
3. Your age
4. Whether you like programming (True/False)

Print them all on one line using f-strings.