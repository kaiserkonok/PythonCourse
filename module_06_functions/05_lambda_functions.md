# Lambda Functions: Writing One-Liner Anonymous Functions

## Learning Objectives

- Create lambda functions
- Understand anonymous functions
- Use lambdas with built-in functions

## What is a Lambda?

A lambda is an **anonymous function** (one-line):

```python
# Named function
def add(a, b):
    return a + b

# Lambda
add = lambda a, b: a + b
```

## Lambda Syntax

```python
lambda parameters: expression
```

```python
# Simple lambda
double = lambda x: x * 2

# Two parameters
add = lambda a, b: a + b

# With multiple expressions (not allowed!)
# lambdas are single expressions only
```

## Using Lambdas

```python
# Lambda assigned to variable
multiply = lambda a, b: a * b
print(multiply(3, 4))  # 12

# Lambda without name (anonymous)
print((lambda x: x * 2)(5))  # 10
```

## Lambdas with Built-in Functions

```python
# sorted() with key
names = ["Bob", "Alice", "Charlie"]
print(sorted(names))  # Alphabetical
print(sorted(names, key=lambda x: len(x)))  # By length: Bob, Alice, Charlie
```

```python
# map() - apply to all
numbers = [1, 2, 3]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)  # [2, 4, 6]
```

```python
# filter() - keep matching
numbers = [1, 2, 3, 4, 5]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4]
```

```python
# sorted() with multiple keys
people = [("Alice", 25), ("Bob", 30), ("Charlie", 25)]
# Sort by age, then name
sorted_people = sorted(people, key=lambda x: (x[1], x[0]))
print(sorted_people)
```

## Code Examples

```python
# Example 1: Simple lambda
square = lambda x: x ** 2
print(square(5))  # 25

# Example 2: Lambda with multiple args
full_name = lambda first, last: f"{first} {last}"
print(full_name("John", "Doe"))

# Example 3: Using with sorted()
words = ["longword", "cat", "elephant"]
print(sorted(words, key=lambda w: len(w)))  # cat, longword, elephant

# Example 4: Using with map()
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # [1, 4, 9, 16, 25]

# Example 5: Using with filter()
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd = list(filter(lambda x: x % 2 != 0, numbers))
print(odd)  # [1, 3, 5, 7, 9]
```

## Lambda vs def

| Lambda | def |
|--------|------|
| One line only | Multiple lines |
| No name (anonymous) | Has name |
| Returns expression | Returns anything |
| Limited | Full power |

## When to Use Lambdas

- **Short functions** - simple operations
- **Callbacks** - for sorted(), map(), filter()
- **One-time use** - don't need to reuse

## Key Takeaways

1. **lambda** keyword creates anonymous function
2. **Single expression** only (no statements)
3. **Used with** sorted(), map(), filter()
4. **Not for complex logic**
5. **More Pythonic** for simple operations

## Practice Exercise

1. Create a lambda that doubles a number
2. Create a lambda that checks if even
3. Use lambda with sorted() to sort by custom order
4. Use lambda with map() to transform a list