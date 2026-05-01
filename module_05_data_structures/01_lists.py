# Code examples from "Lists" lesson

# Example 1: Create and access
colors = ["red", "green", "blue"]
print(colors[0])    # red
print(colors[-1])    # blue

# Example 2: Modify list
colors[0] = "yellow"
print(colors)        # ["yellow", "green", "blue"]

# Example 3: Add/remove items
colors.append("purple")
colors.append("orange")
print(colors)        # ["yellow", "green", "blue", "purple", "orange"]

colors.remove("green")  # Remove by value
print(colors)          # ["yellow", "blue", "purple", "orange"]

popped = colors.pop()   # Remove last
print(popped)          # orange
print(colors)          # ["yellow", "blue", "purple"]

# Example 4: List slicing
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[2:7])   # [2, 3, 4, 5, 6]
print(numbers[::2])    # [0, 2, 4, 6, 8] (every 2nd)
print(numbers[::-1])  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] (reverse)

# Example 5: List operations
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print(combined)         # [1, 2, 3, 4, 5, 6]

print([1] * 3)        # [1, 1, 1] (repeat)


# =====================
# PRACTICE EXERCISE
# =====================

# 1. Create a list of 5 fruits
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# 2. Print the first and last fruit
print(f"First: {fruits[0]}")
print(f"Last: {fruits[-1]}")

# 3. Add a new fruit to the end
fruits.append("fig")
print(f"After adding fig: {fruits}")

# 4. Print a slice of 3 fruits from the middle
print(f"Slice: {fruits[1:4]}")