"""
While Loops (Repeating Until Done)
────────────────────────────────────────────────────────────────────────────
Code examples and practice exercises from the lesson.
────────────────────────────────────────────────────────────────────────────
"""

# Example 1 — Basic While Loop
count = 0

while count < 5:
    print(f"Count: {count}")
    count += 1  # Don't forget this!

print("Done!")


# Example 2 — User Input Validation
# (Commented out to avoid blocking in automated runs)
# while True:
#     age = input("Enter your age (positive number): ")
#     if age.isdigit() and int(age) > 0:
#         age = int(age)
#         break
#     print("Invalid input. Try again.")
#
# print(f"Age: {age}")


# Example 3 — Countdown
seconds = 5

while seconds > 0:
    print(f"{seconds}...")
    seconds -= 1

print("Go! 🚀")


# Example 4 — `break` and `continue`
# break — exit the loop early
i = 0
while i < 10:
    i += 1
    if i == 5:
        break
    print(i)  # 1, 2, 3, 4

print("---")

# continue — skip to next iteration
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)  # 1, 2, 4, 5 (skips 3)


# Example 5 — While with `else`
# The `else` block runs when the loop finishes normally
# (not when broken with `break`)

n = 3

while n > 0:
    print(f"Countdown: {n}")
    n -= 1
else:
    print("Liftoff! 🚀")


# Example 6 — Nested While Loops
# Multiplication table
row = 1

while row <= 3:
    col = 1
    while col <= 3:
        print(f"{row} x {col} = {row * col}")
        col += 1
    print("---")
    row += 1


# ═══════════════════════════════════════════════════════════════════════════════
# PRACTICE EXERCISE
# ═══════════════════════════════════════════════════════════════════════════════
# 1. Use a while loop to print numbers 1 to 10
# 2. Create a loop that asks for a number until the user enters 0
# 3. Use break to stop a loop when a condition is met
# 4. Use continue to skip even numbers in a loop
# ═══════════════════════════════════════════════════════════════════════════════

# 1. Print 1 to 10
num = 1
while num <= 10:
    print(num)
    num += 1

# 2. Ask for number until 0 (simulated with list)
user_inputs = [5, 3, 8, 0]  # Simulated user input
idx = 0
while idx < len(user_inputs):
    val = user_inputs[idx]
    idx += 1
    print(f"Got: {val}")
    if val == 0:
        print("Zero entered, stopping.")
        break

# 3. Use break to stop
counter = 0
while counter < 100:
    counter += 1
    if counter == 7:
        print(f"Stopped at {counter}")
        break

# 4. Use continue to skip even numbers
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(f"Odd: {i}")

# Try modifying it:
# - Use a while loop to calculate factorial of 5
n = 5
factorial = 1
while n > 0:
    factorial *= n
    n -= 1
print(f"Factorial of 5: {factorial}")
