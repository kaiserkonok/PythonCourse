# Code examples from "Recursion" lesson

# Example 1: Simple countdown
def countdown(n):
    if n <= 0:
        print("Done!")
        return
    print(n)
    countdown(n - 1)

print("With 3:")
countdown(3)

print("---")

# Example 2: Calculate factorial
# 5! = 5 * 4 * 3 * 2 * 1 = 120
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(f"5! = {factorial(5)}")

print("---")

# Example 3: Calculate sum to n
def sum_to(n):
    if n <= 1:
        return 1
    return n + sum_to(n - 1)

print(f"Sum to 5: {sum_to(5)}")  # 1+2+3+4+5=15

print("---")

# Example 4: Count elements in list
def count_list(items):
    if not items:
        return 0
    return 1 + count_list(items[1:])

print(f"Count: {count_list([1, 2, 3, 4, 5])}")

print("---")

# Example 5: Fibonacci
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print("Fibonacci sequence:")
for i in range(10):
    print(fibonacci(i), end=" ")
print()


# =====================
# PRACTICE EXERCISE
# =====================

# 1. Create a recursive function to calculate powers (2^n)
def power_of_two(n):
    if n == 0:
        return 1
    return 2 * power_of_two(n - 1)

print(f"2^5 = {power_of_two(5)}")

# 2. Count from 1 to n recursively
def count_up(n, current=1):
    if current > n:
        return
    print(current)
    count_up(n, current + 1)

print("Count to 5:")
count_up(5)

# 3. Find the maximum in a list recursively
def find_max(items):
    if len(items) == 1:
        return items[0]
    if items[0] > find_max(items[1:]):
        return items[0]
    else:
        return find_max(items[1:])

numbers = [5, 2, 8, 1, 9]
print(f"Max: {find_max(numbers)}")

# 4. Calculate the sum of a list recursively
def sum_list(items):
    if not items:
        return 0
    return items[0] + sum_list(items[1:])

print(f"Sum: {sum_list([1, 2, 3, 4, 5])}")