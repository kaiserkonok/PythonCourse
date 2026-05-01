# Code examples from "Arithmetic Operators" lesson

# Example 1: Basic operations
a = 15
b = 4
print(a + b)     # 19
print(a - b)     # 11
print(a * b)     # 60
print(a / b)     # 3.75
print(a // b)    # 3
print(a % b)     # 3
print(a ** b)    # 50625 (15^4)

# Example 2: Order of operations (PEMDAS)
result = 2 + 3 * 4
print(result)  # 14 (not 20)

# Use parentheses to control
result = (2 + 3) * 4
print(result)  # 20

# Example 3: Compound assignments
x = 10
x += 5          # x = x + 5
print(x)        # 15

x -= 3          # x = x - 3
print(x)        # 12

x *= 2          # x = x * 2
print(x)        # 24

# Example 4: Practical uses
seconds = 185
minutes = seconds // 60
remaining_seconds = seconds % 60
print(f"{minutes} min {remaining_seconds} sec")  # 3 min 5 sec


# =====================
# PRACTICE EXERCISE
# =====================

# 1. Use floor division to calculate how many complete hours in 185 minutes
total_minutes = 185
hours = total_minutes // 60
print(f"Complete hours: {hours}")

# 2. Use modulo to get the remaining minutes
remaining_minutes = total_minutes % 60
print(f"Remaining minutes: {remaining_minutes}")

# 3. Calculate 2^10 using **
result = 2 ** 10
print(f"2^10 = {result}")

# 4. Check if 42 is even or odd using modulo
number = 42
if number % 2 == 0:
    print(f"{number} is Even")
else:
    print(f"{number} is Odd")