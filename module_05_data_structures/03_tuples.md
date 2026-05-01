# Tuples: Understanding Immutability and Data Integrity

## Learning Objectives

- Create and use tuples
- Understand immutability
- Know when to use tuples vs lists

## What is a Tuple?

A tuple is an **immutable ordered sequence**:

- Ordered: Items have specific positions
- Immutable: Cannot change after creation
- Can contain different types

```python
# Tuple with parentheses (optional for 2+ items)
coordinates = (10, 20)
mixed = (1, "hello", 3.14)
single = (5,)  # Comma needed for single item!
```

## Tuple vs List

| Feature | Tuple | List |
|---------|-------|------|
| Mutable | No | Yes |
| Syntax | () | [] |
| Performance | Faster | Slightly slower |
| Use case | Fixed data | Changing data |

## Accessing Tuples

```python
point = (10, 20, 30)

print(point[0])   # 10
print(point[1])   # 20
print(point[-1])  # 30
print(point[0:2])  # (10, 20) - slicing returns tuple
```

## Tuple Methods

```python
info = (1, 2, 3, 2, 2)

print(info.count(2))   # 3 (count occurrences)
print(info.index(3))   # 2 (first position of value)
```

## Code Examples

```python
# Example 1: Create tuple
person = ("Alice", 25, "NYC")
print(person)  # ("Alice", 25, "NYC")

# Example 2: Tuple without parentheses
coords = 10, 20, 30
print(coords)  # (10, 20, 30)

# Example 3: Single element tuple (note the comma!)
single = (5,)
print(single)  # (5,)

# Example 4: Unpacking
point = (10, 20, 30)
x, y, z = point
print(f"x={x}, y={y}, z={z}")

# Example 5: Tuple in functions (return multiple values)
def get_stats(numbers):
    return min(numbers), max(numbers), sum(numbers)

result = get_stats([1, 2, 3])
print(result)  # (1, 3, 6)
min_val, max_val, total = result
print(f"Min: {min_val}, Max: {max_val}, Total: {total}")
```

## When to Use Tuples

```python
# ✅ Good: Coordinates (fixed pairs)
location = (40.7128, -74.0060)

# ✅ Good: Function returning multiple values
def divide(a, b):
    return a // b, a % b  # quotient, remainder

quotient, remainder = divide(10, 3)

# ✅ Good: Dictionary keys (tuples are hashable)
inventory = {("apple", "red"): 5, ("banana", "yellow"): 3}

# ❌ Bad: When you need to modify
# Use list when: appending, removing, changing items
```

## Key Takeaways

1. **Tuples use ()** - parentheses
2. **Immutable** - cannot change after creation
3. **Faster than lists** - good for fixed data
4. **Unpacking** - assign to multiple variables
5. **Return multiple values** - from functions

## Practice Exercise

1. Create a tuple with your name, age, city
2. Unpack it into 3 variables
3. Try to modify an element (see the error!)
4. Return multiple values from a function