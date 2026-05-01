# Code examples from "List Comprehensions" lesson

# Example 1: Basic comprehension
numbers = [1, 2, 3, 4, 5]
doubled = [x * 2 for x in numbers]
print(doubled)  # [2, 4, 6, 8, 10]

# Example 2: With range
squares = [x**2 for x in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]

# Example 3: With condition
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [x for x in numbers if x % 2 == 0]
print(evens)  # [2, 4, 6, 8, 10]

# Example 4: String manipulation
text = "hello world"
letters = [char.upper() for char in text if char != " "]
print(letters)  # ["H", "E", "L", "L", "O", "W", "O", "R", "L", "D"]

# Example 5: Nested comprehension (flatten)
matrix = [[1, 2], [3, 4]]
flat = [num for row in matrix for num in row]
print(flat)  # [1, 2, 3, 4]


# =====================
# PRACTICE EXERCISE
# =====================

# 1. Create a list of cubes for numbers 1-5 using comprehension
cubes = [x**3 for x in range(1, 6)]
print(f"Cubes: {cubes}")  # [1, 8, 27, 64, 125]

# 2. Filter a list to only include numbers > 5
numbers = [1, 10, 3, 8, 5, 12, 7]
filtered = [x for x in numbers if x > 5]
print(f"Filtered: {filtered}")  # [10, 8, 12]

# 3. Create a list of first 10 even numbers
evens = [x for x in range(2, 21, 2)]
print(f"First 10 evens: {evens}")  # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# 4. Extract vowels from a sentence
sentence = "hello world how are you"
vowels = [char for char in sentence if char in "aeiou"]
print(f"Vowels: {vowels}")  # ['e', 'o', 'o', 'a', 'e', 'o', 'u']