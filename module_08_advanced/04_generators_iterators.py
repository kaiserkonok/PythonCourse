# Code examples from "Generators & Iterators" lesson

# Example 1: Simple generator
def count_up_to(max):
    current = 1
    while current <= max:
        yield current
        current += 1

for num in count_up_to(3):
    print(num)  # 1, 2, 3

print("---")

# Example 2: Generator vs list comparison
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

print("---")

# Example 3: Using next()
def simple_gen():
    yield "first"
    yield "second"
    yield "third"

gen = simple_gen()
print(next(gen))  # first
print(next(gen))  # second
print(next(gen))  # third

print("---")

# Example 4: Fibonacci generator
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
print("First 10 Fibonacci:")
for _ in range(10):
    print(next(fib), end=" ")
print()

print("---")

# Example 5: Generator expression
gen = (x * 2 for x in range(5))
print(list(gen))  # [0, 2, 4, 6, 8]

# Equivalent list comprehension
comp = [x * 2 for x in range(5)]
print(comp)  # [0, 2, 4, 6, 8]


# =====================
# PRACTICE EXERCISE
# =====================

# 1. Create a simple generator with yield
def my_generator():
    yield "Apple"
    yield "Banana"
    yield "Cherry"

gen = my_generator()
print(f"1: {next(gen)}")
print(f"2: {next(gen)}")
print(f"3: {next(gen)}")

print("---")

# 2. Loop through generator to get values
def count_even(n):
    for i in range(n * 2):
        if i % 2 == 0:
            yield i

print("Even numbers:")
for num in count_even(5):
    print(num, end=" ")
print()

print("---")

# 3. Create a fibonacci generator
def fibonacci_gen(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

print("Fibonacci generator:")
print(list(fibonacci_gen(10)))

# 4. Use generator expression
result = (x**2 for x in range(1, 6))
print("Generator expression:")
print(list(result))