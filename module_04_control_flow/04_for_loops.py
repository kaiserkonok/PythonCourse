# Code examples from "For Loops" lesson

# Example 1: Simple range
for i in range(5):
    print(i)  # 0 1 2 3 4

print("---")

# Example 2: Range with start and stop
for i in range(1, 6):
    print(i)  # 1 2 3 4 5

print("---")

# Example 3: Range with step
for i in range(0, 10, 2):
    print(i)  # 0 2 4 6 8

print("---")

# Example 4: Loop through list
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(f"I like {fruit}")

print("---")

# Example 5: Enumerate (get index and value)
colors = ["red", "green", "blue"]

for index, color in enumerate(colors):
    print(f"{index}: {color}")


# =====================
# PRACTICE EXERCISE
# =====================

# 1. Use for loop to print 1 to 5
print("Numbers 1-5:")
for i in range(1, 6):
    print(i)

print("---")

# 2. Print even numbers 2 to 10
print("Even numbers:")
for i in range(2, 11, 2):
    print(i)

print("---")

# 3. Loop through your name
name = "Alice"
for char in name:
    print(char)

print("---")

# 4. Use enumerate to print index and value of a list
foods = ["pizza", "burger", "sushi"]
for index, food in enumerate(foods):
    print(f"{index}: {food}")