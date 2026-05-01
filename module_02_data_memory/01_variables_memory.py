# Code examples from "Variables & Memory" lesson

# Example 1: Create a variable
player_name = "Mario"
print(player_name)

# Example 2: Reassign a variable
age = 25
print(age)
age = 26  # Overwrites the old value
print(age)

# Example 3: Multiple variables
x = 5
y = 10
z = x + y
print(z)  # Output: 15

# Example 4: Swap values
a = 1
b = 2
a, b = b, a  # Pythonic swap
print(f"a = {a}, b = {b}")  # a = 2, b = 1


# =====================
# PRACTICE EXERCISE
# =====================

# Create variables for:
# 1. Your first name
# 2. Your last name
# 3. Your age
# 4. Whether you like programming (True/False)

# Print them all on one line using f-strings.

# Your code here:
first_name = "Alice"
last_name = "Smith"
my_age = 25
likes_programming = True

print(f"{first_name} {last_name}, age {my_age}, likes programming: {likes_programming}")