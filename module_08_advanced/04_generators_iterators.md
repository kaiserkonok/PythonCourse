# Generators & Iterators: Managing Memory-Efficient Data Streams

## Learning Objectives

- Understand iterators
- Create generators with yield
- Use generators for memory efficiency

## What is an Iterator?

An iterator is an object that can be looped over:

```python
# Lists are iterable (can create iterators)
numbers = [1, 2, 3]
iterator = iter(numbers)

print(next(iterator))  # 1
print(next(iterator))  # 2
print(next(iterator))  # 3
# print(next(iterator))  # StopIteration
```

## What is a Generator?

A generator creates values **one at a time**:

```python
def count_to_3():
    yield 1
    yield 2
    yield 3

for i in count_to_3():
    print(i)
# Output: 1, 2, 3
```

## Generator vs List

| List | Generator |
|------|-----------|
| All values in memory | One value at a time |
| Fast random access | Sequential only |
| Uses more memory | Memory efficient |

```python
# List - all in memory
def get_numbers_list():
    return [1, 2, 3, 4, 5]

# Generator - one at a time
def get_numbers_gen():
    for i in range(1, 6):
        yield i
```

## Code Examples

```python
# Example 1: Simple generator
def count_up_to(max):
    current = 1
    while current <= max:
        yield current
        current += 1

for num in count_up_to(3):
    print(num)  # 1, 2, 3

# Example 2: Generator with return
def first_n(n):
    nums = []
    current = 1
    while len(nums) < n:
        nums.append(current)
        current += 1
    return nums  # Returns list

def first_n_gen(n):
    current = 1
    while n > 0:
        yield current
        current += 1
        n -= 1

print(list(first_n(3)))   # [1, 2, 3]
print(list(first_n_gen(3)))  # [1, 2, 3]
# But generator is more memory efficient!

# Example 3: Using next()
def simple_gen():
    yield "first"
    yield "second"
    yield "third"

gen = simple_gen()
print(next(gen))  # first
print(next(gen))  # second
print(next(gen))  # third

# Example 4: Fibonacci generator
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
for _ in range(10):
    print(next(fib), end=" ")
print()

# Example 5: Generator expression
gen = (x * 2 for x in range(5))
print(list(gen))  # [0, 2, 4, 6, 8]

# Equivalent list comprehension
comp = [x * 2 for x in range(5)]
print(comp)  # [0, 2, 4, 6, 8]
```

## When to Use Generators

- **Large datasets** - don't load all in memory
- **Infinite sequences** - can't pre-compute
- **Streaming data** - process as it arrives
- **Pipeline** - transform step by step

## Key Takeaways

1. **yield** creates a generator
2. **next()** gets next value
3. **StopIteration** - when done
4. **Memory efficient** - one at a time
5. **Generator expression** - (expr for item in iterable)

## Practice Exercise

1. Create a simple generator with yield
2. Loop through generator to get values
3. Create a fibonacci generator
4. Use generator expression