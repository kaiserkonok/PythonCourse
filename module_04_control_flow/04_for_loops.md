# Iteration with For Loops: Walking Through Ranges and Sequences

## Learning Objectives

- Use for loops to iterate over sequences
- Understand range() for generating numbers
- Loop through strings, lists, and other iterables

## What is a For Loop?

A for loop **iterates over each item** in a sequence:

```python
# Loop through a list
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
```

## Using range()

The `range()` function generates a sequence of numbers:

```python
# range(stop)
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# range(start, stop)
for i in range(1, 6):
    print(i)  # 1, 2, 3, 4, 5

# range(start, stop, step)
for i in range(0, 10, 2):
    print(i)  # 0, 2, 4, 6, 8
```

## Loop Through Different Types

```python
# String
for char in "Python":
    print(char)

# List
for item in [1, 2, 3]:
    print(item)

# Tuple
for item in (1, 2, 3):
    print(item)
```

## Code Examples

```python
# Example 1: Simple range
for i in range(5):
    print(i)  # 0 1 2 3 4

# Example 2: Range with start and stop
for i in range(1, 6):
    print(i)  # 1 2 3 4 5

# Example 3: Range with step
for i in range(0, 10, 2):
    print(i)  # 0 2 4 6 8

# Example 4: Loop through list
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(f"I like {fruit}")

# Example 5: Enumerate (get index and value)
colors = ["red", "green", "blue"]

for index, color in enumerate(colors):
    print(f"{index}: {color}")
```

## For vs While Loops

| For Loop | While Loop |
|----------|------------|
| Know iteration count | Unknown count |
| Use range() | Use condition |
| More common | Less common |
| for i in range(5): | while i < 5: |

## Key Takeaways

1. **for** loops iterate over sequences
2. **range(n)** generates 0 to n-1
3. **range(start, stop)** generates start to stop-1
4. **range(start, stop, step)** with step
5. **enumerate()** gives index and value

## Practice Exercise

1. Use for loop to print 1 to 5
2. Print even numbers 2 to 10
3. Loop through your name
4. Use enumerate to print index and value of a list