# List Comprehensions: The Pythonic Way to Generate Lists

## Learning Objectives

- Understand list comprehensions
- Create lists more efficiently
- Use conditional logic in comprehensions

## What is a List Comprehension?

A list comprehension creates a list **in a single line**:

```python
# Traditional way
squares = []
for i in range(5):
    squares.append(i**2)

# Pythonic way (comprehension)
squares = [i**2 for i in range(5)]
```

## Basic Syntax

```
[expression for item in iterable]
```

```python
# Create list of squares
squares = [x**2 for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]

# Create list of strings
words = [word.upper() for word in ["hello", "world"]]
print(words)  # ["HELLO", "WORLD"]
```

## With Condition

```python
# [expression for item in iterable if condition]
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8]
```

## Code Examples

```python
# Example 1: Basic comprehension
numbers = [1, 2, 3, 4, 5]
doubled = [x * 2 for x in numbers]
print(doubled)  # [2, 4, 6, 8, 10]

# Example 2: With range
squares = [x**2 for x in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]

# Example 3: With condition
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [x for x in numbers if x % 2 == 0]
print(evens)  # [2, 4, 6, 8, 10]

# Example 4: String manipulation
text = "hello world"
letters = [char.upper() for char in text if char != " "]
print(letters)  # ["H", "E", "L", "L", "O", "W", "O", "R", "L", "D"]

# Example 5: Nested comprehension (flatten)
matrix = [[1, 2], [3, 4]]
flat = [num for row in matrix for num in row]
print(flat)  # [1, 2, 3, 4]
```

## List Comprehension vs For Loop

| For Loop | List Comprehension |
|----------|-----------------|
| Multiple lines | One line |
| Easier to read for complex logic | Clean for simple transformations |
| More flexible | Less flexible |

## Key Takeaways

1. **Clean syntax** - [expr for item in iterable]
2. **With if** - [expr for item in iterable if condition]
3. **Faster than loops** for simple operations
4. **More Pythonic** - preferred style
5. **Readable** for straightforward patterns

## Practice Exercise

1. Create a list of cubes for numbers 1-5 using comprehension
2. Filter a list to only include numbers > 5
3. Create a list of first 10 even numbers
4. Extract vowels from a sentence