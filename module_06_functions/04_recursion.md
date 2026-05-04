# 🔄 Recursion: Functions That Call Themselves

<p align="center">
  <img src="https://img.shields.io/badge/recursive-Self%20Calling-blue?style=flat-square" alt="recursive">
  <img src="https://img.shields.io/badge/Base%20Case-Stop%20Condition-green?style=flat-square" alt="Base Case">
  <img src="https://img.shields.io/badge/Stack-Deep%20Calls-orange?style=flat-square" alt="Stack">
</p>

> ### 💡 Recursion is like looking in a mirror that reflects a mirror. A function calls itself, breaking big problems into smaller copies of the same problem.
> Learn the power and danger of recursive functions.

---

## 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- ✅ Understand the concept of recursion
- ✅ Write recursive functions with base cases
- ✅ Recognize when to use recursion vs iteration

---

## 🧠 Mental Model: Russian Nesting Dolls

Recursion is like opening **Russian nesting dolls**:

```
1. Open the big doll (problem)
2. Inside is a smaller doll (same problem, smaller)
3. Keep opening until you reach the tiniest doll (base case)
4. Then work your way back out, combining results
```

Every recursive function needs a **base case** — the smallest version that stops the recursion.

---

## 📖 The Recipe

```python
def recursive_function(input):
    # 1. Base case — when to stop
    if simple_condition:
        return simple_result

    # 2. Recursive case — break into smaller problem
    smaller_result = recursive_function(smaller_input)

    # 3. Combine results
    return combine(smaller_result)
```

---

## 📊 Recursion vs Iteration

| Feature | Recursion | Iteration (Loops) |
|---------|-----------|------------------|
| **Syntax** | Function calls itself | `for` or `while` loop |
| **Readability** | Often cleaner for trees/graphs | Simpler for lists |
| **Memory** | Uses call stack | Constant memory |
| **Speed** | Slightly slower | Usually faster |

---

## ⚠️ Common Mistakes

```
❌ Missing base case
   def factorial(n):
       return n * factorial(n - 1)  ← No base case → infinite recursion!

❌ Wrong base case
   def countdown(n):
       if n == 1:      ← Stops at 1, misses 0!
           return
       countdown(n - 1)

❌ Recursion depth exceeded
   Python limit is ~1000 calls
   RecursionError: maximum recursion depth exceeded
   → Use iteration for deep problems

❌ Not combining results
   def sum_list(lst):
       if not lst: return 0
       sum_list(lst[1:])  ← Forgets to add first element!
```

---

## 💻 Code Examples

### 📌 Example 1 — Factorial

```python
def factorial(n):
    """n! = n × (n-1) × ... × 1"""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # 120
```

### 📌 Example 2 — Fibonacci

```python
def fibonacci(n):
    """Returns nth Fibonacci number."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))  # 55
```

### 📌 Example 3 — Sum of List

```python
def sum_list(lst):
    if not lst:
        return 0
    return lst[0] + sum_list(lst[1:])

print(sum_list([1, 2, 3, 4, 5]))  # 15
```

### 📌 Example 4 — Countdown

```python
def countdown(n):
    if n <= 0:
        print("Liftoff! 🚀")
        return
    print(n)
    countdown(n - 1)

countdown(5)
```

### 📌 Example 5 — Flattening Nested Lists

```python
def flatten(nested):
    result = []
    for item in nested:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

data = [1, [2, 3], [4, [5, 6]]]
print(flatten(data))  # [1, 2, 3, 4, 5, 6]
```

### 📌 Example 6 — Binary Search

```python
def binary_search(arr, target, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    if low > high:
        return -1  # Not found

    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, high)
    else:
        return binary_search(arr, target, low, mid - 1)

nums = [1, 3, 5, 7, 9, 11]
print(binary_search(nums, 7))  # 3
```

---

## 🧪 Practice Exercise

1. Write a recursive function to calculate the power of a number (x^n)
2. Create a recursive function that counts down from n to 0
3. Write a function to check if a string is a palindrome using recursion
4. Create a recursive function to find the maximum value in a list

---

## 📋 Key Takeaways

| Concept | Takeaway |
|---------|----------|
| 🔄 **Recursion** | A function that calls itself |
| 🛑 **Base case** | Required — stops the infinite loop |
| 📉 **Recursive case** | Breaks problem into smaller version |
| ⚠️ **Depth limit** | Python limits recursion depth (~1000) |
| 🌳 **Best for** | Trees, graphs, divide-and-conquer problems |

---

## 🔗 Further Reading

- 📖 [Recursion — Official Docs](https://docs.python.org/3/faq/programming.html#how-do-i-write-a-function-with-output-parameters-call-by-reference)
- 🌟 [Recursive Functions — Real Python](https://realpython.com/python-thinking-recursively/)
- 🔧 [Recursion Limit — sys module](https://docs.python.org/3/library/sys.html#sys.setrecursionlimit)