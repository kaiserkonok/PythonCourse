# Code examples from "Conditional Branching" lesson

# Example 1: Basic if
is_raining = True

if is_raining:
    print("Bring an umbrella!")

# Example 2: if-else
temperature = 30

if temperature > 25:
    print("It's hot!")
else:
    print("It's comfortable")

# Example 3: if-elif-else
age = 25

if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
elif age < 60:
    print("Adult")
else:
    print("Senior")

# Example 4: Nested conditions
age = 25
has_money = True

if age >= 18:
    if has_money:
        print("You can buy it!")
    else:
        print("You can't afford it")
else:
    print("Too young")

# Example 5: Multiple elif
day = "Monday"

if day == "Monday":
    print("Start of week")
elif day == "Friday":
    print("End of week")
elif day == "Saturday" or day == "Sunday":
    print("Weekend!")
else:
    print("Midweek")


# =====================
# PRACTICE EXERCISE
# =====================

# 1. Create a grading system (A, B, C, D, F) using if-elif-else
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score {score} = Grade {grade}")

# 2. Check if a number is positive, negative, or zero
number = -5

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")

# 3. Create a simple login check with username and password
username = "admin"
password = "password123"

if username == "admin" and password == "password123":
    print("Login successful!")
else:
    print("Login failed")