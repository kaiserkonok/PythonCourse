# Code examples from "While Loops" lesson

# Example 1: Count 0 to 4
count = 0

while count < 5:
    print(count)
    count += 1
# Output: 0 1 2 3 4

# Example 2: Countdown
count = 5

while count > 0:
    print(count)
    count -= 1

print("Blast off!")

# Example 3: Sum numbers until negative (uncomment to test)
# total = 0

# while True:
#     num = int(input("Enter number (-1 to quit): "))
#     if num < 0:
#         break
#     total += num
#     print(f"Running total: {total}")

# Example 4: Menu loop
choice = ""

while choice != "3":
    print("\n1. Say hello")
    print("2. Say goodbye")
    print("3. Quit")
    choice = input("Choose: ")
    
    if choice == "1":
        print("Hello!")
    elif choice == "2":
        print("Goodbye!")

print("Exited!")

# Example 5: Only continue if valid
age = 25  # Simulating valid input

while age < 1 or age > 120:
    age = int(input("Enter valid age: "))

print(f"You are {age} years old")


# =====================
# PRACTICE EXERCISE
# =====================

# 1. Print numbers 1 to 10 using while loop
count = 1
while count <= 10:
    print(count)
    count += 1

print("---")

# 2. Create a countdown from 10 to 1
count = 10
while count > 0:
    print(count)
    count -= 1
print("Blast off!")

print("---")

# 3. Ask for input until user enters "quit" (simulated)
# response = ""
# while response != "quit":
#     response = input("Enter 'quit' to exit: ")

# 4. Calculate sum of 0 to 100 using while loop
total = 0
i = 0
while i <= 100:
    total += i
    i += 1

print(f"Sum of 0 to 100: {total}")