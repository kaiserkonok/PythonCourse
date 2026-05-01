# Code examples from "Loop Control" lesson

# Example 1: break - find first match
fruits = ["apple", "banana", "cherry", "date"]

for fruit in fruits:
    if fruit == "cherry":
        print(f"Found {fruit}!")
        break
    else:
        print(f"Not {fruit}")

print("---")

# Example 2: continue - skip even numbers
for i in range(10):
    if i % 2 == 0:
        continue
    print(f"Odd: {i}")  # 1 3 5 7 9

print("---")

# Example 3: pass - placeholder
class MyClass:
    pass  # Will add methods later

print("MyClass created!")

# Example 4: break in while loop
count = 0

while True:
    print(count)
    count += 1
    if count >= 5:
        break

print("---")

# Example 5: continue in while loop
count = 0

while count < 5:
    count += 1
    if count == 3:
        continue
    print(count)  # 1 2 4 5 (skips 3)


# =====================
# PRACTICE EXERCISE
# =====================

# 1. Find the first number divisible by 7 from 1-50
for i in range(1, 51):
    if i % 7 == 0:
        print(f"First divisible by 7: {i}")
        break

print("---")

# 2. Print all numbers 1-10 except multiples of 3
for i in range(1, 11):
    if i % 3 == 0:
        continue
    print(i)  # 1 2 4 5 7 8 10

print("---")

# 3. Use pass in a for loop that prints nothing
for i in range(5):
    pass  # No output

print("Loop completed (did nothing)")

# 4. Combine break and continue in one loop
for i in range(10):
    if i == 2:
        continue  # Skip 2
    if i == 7:
        print("Found 7, stopping!")
        break  # Stop at 7
    print(i)  # 0 1 3 4 5 6