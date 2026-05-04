"""
Match-Case (Python's Switch Statement)
────────────────────────────────────────────────────────────────────────────
Code examples and practice exercises from the lesson.
────────────────────────────────────────────────────────────────────────────
"""

# Example 1 — Basic Match
status = "shipped"

match status:
    case "pending":
        print("Your order is waiting")
    case "shipped":
        print("Your order is on the way")
    case "delivered":
        print("Your order has arrived")
    case _:
        print("Unknown status")


# Example 2 — Multiple Values
day = "Saturday"

match day:
    case "Saturday" | "Sunday":
        print("Weekend!")
    case "Monday":
        print("Start of the week")
    case "Friday":
        print("Almost weekend")
    case _:
        print("Regular weekday")


# Example 3 — With Guards
score = 85

match score:
    case n if n >= 90:
        print("A")
    case n if n >= 80:
        print("B")
    case n if n >= 70:
        print("C")
    case _:
        print("F")


# Example 4 — HTTP Status Codes
status_code = 404

match status_code:
    case 200:
        print("OK")
    case 301 | 302:
        print("Redirect")
    case 400:
        print("Bad Request")
    case 404:
        print("Not Found")
    case 500:
        print("Server Error")
    case _:
        print("Unknown status")


# Example 5 — Comparing to `if/elif`
# Old way (verbose)
role = "admin"
if role == "admin":
    print("Full access")
elif role == "editor":
    print("Edit access")
elif role == "viewer":
    print("Read-only")
else:
    print("No access")

# New way (clean)
match role:
    case "admin":
        print("Full access")
    case "editor":
        print("Edit access")
    case "viewer":
        print("Read-only")
    case _:
        print("No access")


# Example 6 — Tuple Matching
point = (3, 5)

match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"On Y-axis at {y}")
    case (x, 0):
        print(f"On X-axis at {x}")
    case (x, y):
        print(f"At point ({x}, {y})")


# ═══════════════════════════════════════════════════════════════════════════════
# PRACTICE EXERCISE
# ═══════════════════════════════════════════════════════════════════════════════
# 1. Use match/case to convert a number (1-7) to a day name
# 2. Match a grade letter (A-F) to a message
# 3. Use the | operator to group cases
# 4. Use a guard to add extra conditions
# ═══════════════════════════════════════════════════════════════════════════════

# 1. Number to day name
day_num = 3

match day_num:
    case 1:
        day_name = "Monday"
    case 2:
        day_name = "Tuesday"
    case 3:
        day_name = "Wednesday"
    case 4:
        day_name = "Thursday"
    case 5:
        day_name = "Friday"
    case 6 | 7:
        day_name = "Weekend"
    case _:
        day_name = "Invalid day"

print(f"Day: {day_name}")

# 2. Grade to message
grade = "B"

match grade:
    case "A":
        msg = "Excellent!"
    case "B":
        msg = "Good job!"
    case "C":
        msg = "Average"
    case "D":
        msg = "Needs improvement"
    case _:
        msg = "Failed"

print(f"Grade message: {msg}")

# 3. Group cases with |
season = "summer"

match season:
    case "spring" | "summer":
        print("Warm season")
    case "fall" | "winter":
        print("Cool season")
    case _:
        print("Unknown season")

# 4. Guard
age = 25

match age:
    case n if n < 18:
        print("Too young")
    case n if n <= 65:
        print("Eligible")
    case _:
        print("Senior discount")

# Try modifying it:
# - Combine tuple matching with guards
location = (10, 20)

match location:
    case (x, y) if x > 0 and y > 0:
        print(f"First quadrant at ({x}, {y})")
    case (x, y) if x < 0 and y > 0:
        print(f"Second quadrant at ({x}, {y})")
    case _:
        print("Other quadrant")
