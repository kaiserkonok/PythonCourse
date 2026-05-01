# Code examples from "Lambda Functions" lesson

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


# =====================
# PRACTICE EXERCISE
# =====================

# 1. Create a lambda that doubles a number
double = lambda x: x * 2
print(f"Double 5: {double(5)}")

# 2. Create a lambda that checks if even
is_even = lambda x: x % 2 == 0
print(f"Is 4 even: {is_even(4)}")
print(f"Is 5 even: {is_even(5)}")

# 3. Use lambda with sorted() to sort by custom order
pairs = [("a", 3), ("b", 1), ("c", 2)]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print(f"Sorted by second element: {sorted_pairs}")

# 4. Use lambda with map() to transform a list
names = ["alice", "bob", "charlie"]
capitalized = list(map(lambda x: x.capitalize(), names))
print(f"Capitalized: {capitalized}")