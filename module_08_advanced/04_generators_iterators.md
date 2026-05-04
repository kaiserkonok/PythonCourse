# 🌀 Generators & Iterators: Lazy Evaluation

<p align="center">
  <img src="https://img.shields.io/badge/yield-Generator-blue?style=flat-square" alt="yield">
  <img src="https://img.shields.io/badge/Iterator-Next%20Item-green?style=flat-square" alt="Iterator">
  <img src="https://img.shields.io/badge/Memory-Efficient-orange?style=flat-square" alt="Efficient">
</p>

> ### 💡 Generators produce values one at a time, on demand. Like a streaming service — you get data as you need it, not all at once.
> Learn how to write memory-efficient code with generators.

---

## 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- ✅ Create generator functions using `yield`
- ✅ Use generator expressions for lazy evaluation
- ✅ Understand the difference between iterators and generators
- ✅ Know when to use generators vs lists

---

## 🧠 Mental Model: A Streaming Service

Generators are like **Netflix streaming**:

```
📺 List = Download entire season (uses lots of memory)
🌀 Generator = Stream one episode at a time (uses little memory)
```

You get data only when you ask for it — not all at once.

---

## 📖 Generator Functions

```python
def count_up_to(n):
    i = 1
    while i <= n:
        yield i  # Pause here, return value
        i += 1   # Resume here next time

# Use it
for num in count_up_to(5):
    print(num)  # 1, 2, 3, 4, 5
```

---

## 📊 Generator vs List

| Feature | List | Generator |
|---------|------|-----------|
| **Memory** | Stores all values | One value at a time |
| **Speed** | Fast to access | Slightly slower per item |
| **Reuse** | Can iterate multiple times | Single use only |
| **Size** | `len()` works | No `len()` |

---

## ⚠️ Common Mistakes

```
❌ Trying to reuse a generator
   gen = (x for x in range(3))
   list(gen)  # [0, 1, 2]
   list(gen)  # [] (empty — already consumed!)

❌ Using return instead of yield
   def bad():
       return 1  ← Returns and stops
       return 2  ← Never reached
   def good():
       yield 1   ← Returns, but remembers position
       yield 2   ← Next call continues here

❌ Generator expressions vs list comprehensions
   [x**2 for x in range(10)]  ← List (stores all)
   (x**2 for x in range(10))  ← Generator (lazy)

❌ Infinite generators without break
   def infinite():
       while True:
           yield 1  ← Never stops!
   for x in infinite():  ← Infinite loop
```

---

## 💻 Code Examples

### 📌 Example 1 — Basic Generator

```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for num in countdown(5):
    print(num)  # 5, 4, 3, 2, 1
```

### 📌 Example 2 — Generator Expression

```python
# List comprehension (eager)
squares_list = [x**2 for x in range(5)]
print(squares_list)  # [0, 1, 4, 9, 16]

# Generator expression (lazy)
squares_gen = (x**2 for x in range(5))
print(next(squares_gen))  # 0
print(next(squares_gen))  # 1
```

### 📌 Example 3 — Memory Efficiency

```python
import sys

# List — stores all 1M items
big_list = [x for x in range(1_000_000)]
print(f"List: {sys.getsizeof(big_list)} bytes")

# Generator — stores only state
big_gen = (x for x in range(1_000_000))
print(f"Generator: {sys.getsizeof(big_gen)} bytes")
```

### 📌 Example 4 — Infinite Generator

```python
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Get first 10 fibonacci numbers
fib = fibonacci()
for _ in range(10):
    print(next(fib), end=" ")
```

### 📌 Example 5 — Pipeline with Generators

```python
def read_data():
    for i in range(1, 6):
        yield i

def filter_odd(data):
    for item in data:
        if item % 2 == 1:
            yield item

def double(data):
    for item in data:
        yield item * 2

# Chain generators
pipeline = double(filter_odd(read_data()))
print(list(pipeline))  # [2, 6, 10]
```

### 📌 Example 6 — `yield from`

```python
def chain(*iterables):
    for it in iterables:
        yield from it

result = list(chain([1, 2], [3, 4], [5, 6]))
print(result)  # [1, 2, 3, 4, 5, 6]
```

---

## 🧪 Practice Exercise

1. Create a generator that yields even numbers up to n
2. Use a generator expression to sum squares of 1-100
3. Create a generator that yields prime numbers
4. Chain two generators together

---

## 📋 Key Takeaways

| Concept | Takeaway |
|---------|----------|
| 🌀 **yield** | Pauses function, returns value, resumes later |
| ⚡ **Lazy** | Values produced on demand, not all at once |
| 💾 **Memory** | Generators use minimal memory |
| 🔁 **Single use** | Generators can only be iterated once |
| 🔗 **Pipeline** | Chain generators for data processing |

---

## 🔗 Further Reading

- 📖 [Generators — Official Docs](https://docs.python.org/3/tutorial/classes.html#generators)
- 🌟 [Generators vs Iterators — Real Python](https://realpython.com/introduction-to-python-generators/)
- 🔧 [yield from — docs](https://docs.python.org/3/reference/expressions.html#yield-expressions)