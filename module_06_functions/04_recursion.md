# Recursion: Functions That Call Themselves

## Learning Objectives

- Understand recursion
- Create recursive functions
- Avoid infinite recursion with base cases

## What is Recursion?

Recursion is when a function **calls itself**:

```python
def countdown(n):
    if n <= 0:
        print("Done!")
    else:
        print(n)
        countdown(n - 1)  # Calls itself!

countdown(3)
# Output: 3, 2, 1, Done!
```

## How Recursion Works

```
countdown(3)
    → print(3)
    → countdown(2)
        → print(2)
        → countdown(1)
            → print(1)
            → countdown(0)
                → print("Done!")
```

## Base Case

The base case **stops the recursion**:

```python
# ❌ Wrong: No base case (infinite loop!)
def bad_countdown(n):
    print(n)
    bad_countdown(n - 1)

# ✅ Correct: Has base case
def good_countdown(n):
    if n <= 0:
        return  # Base case! Stop.
    print(n)
    good_countdown(n - 1)  # Reduces toward base case
```

## Code Examples

```python
# Example 1: Simple countdown
def countdown(n):
    if n <= 0:
        print("Done!")
        return
    print(n)
    countdown(n - 1)

print("With 3:")
countdown(3)

# Example 2: Calculate factorial
# 5! = 5 * 4 * 3 * 2 * 1 = 120
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(f"5! = {factorial(5)}")

# Example 3: Calculate sum to n
def sum_to(n):
    if n <= 1:
        return 1
    return n + sum_to(n - 1)

print(f"Sum to 5: {sum_to(5)}")  # 1+2+3+4+5=15

# Example 4: Count elements in list
def count_list(items):
    if not items:
        return 0
    return 1 + count_list(items[1:])

print(count_list([1, 2, 3, 4, 5]))

# Example 5: Fibonacci
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print("Fibonacci sequence:")
for i in range(10):
    print(fibonacci(i), end=" ")
print()
```

## Recursion vs Iteration

| Recursion | Iteration |
|----------|----------|
| Elegant for mathematical problems | More efficient |
| Can be slower | Faster |
| Risk of infinite loop | Easier to debug |

## Key Takeaways

1. **Function calls itself** - recursive
2. **Base case** - stops recursion
3. **Always move toward base case** - else infinite loop
4. **Use for** - tree traversal, math problems
5. **Iteration is often faster** - choose wisely

## Practice Exercise

1. Create a recursive function to calculate powers (2^n)
2. Count from 1 to n recursively
3. Find the maximum in a list recursively
4. Calculate the sum of a list recursively