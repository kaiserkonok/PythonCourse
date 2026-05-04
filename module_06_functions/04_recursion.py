"""
Recursion (Functions That Call Themselves)
────────────────────────────────────────────────────────────────────────────
Code examples and practice exercises from the lesson.
────────────────────────────────────────────────────────────────────────────
"""

# Example 1 — Factorial
def factorial(n):
    """n! = n × (n-1) × ... × 1"""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # 120


# Example 2 — Fibonacci
def fibonacci(n):
    """Returns nth Fibonacci number."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))  # 55


# Example 3 — Sum of List
def sum_list(lst):
    if not lst:
        return 0
    return lst[0] + sum_list(lst[1:])

print(sum_list([1, 2, 3, 4, 5]))  # 15


# Example 4 — Countdown
def countdown(n):
    if n <= 0:
        print("Liftoff! 🚀")
        return
    print(n)
    countdown(n - 1)

countdown(5)


# Example 5 — Flattening Nested Lists
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


# Example 6 — Binary Search
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


# ═══════════════════════════════════════════════════════════════════════════════
# PRACTICE EXERCISE
# ═══════════════════════════════════════════════════════════════════════════════
# 1. Write a recursive function to calculate the power of a number (x^n)
# 2. Create a recursive function that counts down from n to 0
# 3. Write a function to check if a string is a palindrome using recursion
# 4. Create a recursive function to find the maximum value in a list
# ═══════════════════════════════════════════════════════════════════════════════

# 1. Power
def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)

print(f"2^8 = {power(2, 8)}")

# 2. Countdown (already shown, but here's a variation that returns list)
def count_down_list(n):
    if n <= 0:
        return ["Liftoff!"]
    return [n] + count_down_list(n - 1)

print(count_down_list(3))

# 3. Palindrome
def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

print(f"'racecar' is palindrome: {is_palindrome('racecar')}")
print(f"'hello' is palindrome: {is_palindrome('hello')}")

# 4. Max in list
def find_max(lst):
    if len(lst) == 1:
        return lst[0]
    rest_max = find_max(lst[1:])
    return lst[0] if lst[0] > rest_max else rest_max

print(f"Max: {find_max([3, 1, 4, 1, 5, 9, 2])}")

# Try modifying it:
# - Recursive sum of digits
def sum_digits(n):
    if n < 10:
        return n
    return (n % 10) + sum_digits(n // 10)

print(f"Sum of digits of 1234: {sum_digits(1234)}")
