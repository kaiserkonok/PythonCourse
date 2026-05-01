# Comparison Operators: Evaluating Relationships

## Learning Objectives

- Use comparison operators to compare values
- Understand == vs = (assignment vs comparison)
- Chain comparisons in Python 3

## The Comparison Operators

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| == | Equal to | 10 == 10 | True |
| != | Not equal | 10 != 5 | True |
| > | Greater than | 10 > 5 | True |
| < | Less than | 10 < 5 | False |
| >= | Greater or equal | 10 >= 10 | True |
| <= | Less or equal | 10 <= 5 | False |

## Common Comparisons

```python
# Equality
score = 85
print(score == 100)   # False - not perfect
print(score == 85)    # True - matches

# Not equal
name = "Alice"
print(name != "Bob")  # True

# Greater/Less than
age = 18
print(age >= 18)     # True - can vote
print(age < 21)       # True - cannot drink in US
```

## The == vs = Mistake

This is a common beginner mistake:

```python
# ❌ Wrong: Comparison in if (always True!)
if x = 10:           # SyntaxError in Python!
    print("x is 10")

# ✅ Correct: Assignment then comparison
x = 10
if x == 10:
    print("x is 10")
```

## Chained Comparisons (Python Magic)

Python allows chaining comparisons:

```python
# Traditional way
x = 5
result = 1 < x and x < 10
print(result)  # True

# Pythonic way (chained)
x = 5
result = 1 < x < 10
print(result)  # True - same thing!

# Works with more than 2
x = 7
result = 1 < x < 10 < 20
print(result)  # True
```

## Code Examples

```python
# Example 1: Basic comparisons
a = 10
b = 20
print(a == b)    # False
print(a != b)    # True
print(a > b)     # False
print(a < b)     # True
print(a >= 10)   # True
print(a <= 10)   # True

# Example 2: String comparisons
name1 = "Alice"
name2 = "alice"
print(name1 == name2)     # False (case-sensitive)
print(name1.lower() == name2)  # True

# Example 3: Mixed type comparison
print(10 == "10")        # False (int vs str)
print(10 == 10.0)       # True (int vs float)

# Example 4: In comparisons
text = "Hello Python"
print("Python" in text)  # True
print("python" in text)  # False (case-sensitive)

# Example 5: Checking ranges
score = 75
if 0 <= score <= 100:
    print("Valid score")
else:
    print("Invalid score")
```

## Key Takeaways

1. **==** checks equality, **=** assigns
2. **String comparisons** are case-sensitive
3. **Chained comparisons** work in Python: 1 < x < 10
4. **in** checks if substring exists
5. **Comparisons return booleans** for use in conditionals

## Practice Exercise

1. Create variables for your age and a voting age (18)
2. Check if you can vote
3. Check if two strings are equal
4. Use chained comparison to check if a number is between 1 and 100