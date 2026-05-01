# Code examples from "Match-Case" lesson

# Example 1: Simple status codes
http_code = 404

match http_code:
    case 200:
        print("Success")
    case 301:
        print("Redirect")
    case 404:
        print("Not Found")
    case 500:
        print("Server Error")
    case _:
        print(f"Unknown code: {http_code}")

# Example 2: Multiple values
day = "Saturday"

match day:
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
        print("Weekday")
    case "Saturday" | "Sunday":
        print("Weekend")
    case _:
        print("Invalid day")

# Example 3: Using wildcards
command = "quit"

match command:
    case "start":
        print("Starting...")
    case "stop":
        print("Stopping...")
    case _:
        print("Unknown command")

# Example 4: With conditions (guards)
status = 201

match status:
    case 200 | 201 if status < 300:
        print("Success")
    case 400:
        print("Bad Request")
    case 500:
        print("Server Error")
    case _:
        print("Other")

# Example 5: Check multiple patterns
response = "yes"

match response.lower():
    case "yes" | "y" | "true":
        print("Confirmed")
    case "no" | "n" | "false":
        print("Declined")
    case _:
        print("Invalid response")


# =====================
# PRACTICE EXERCISE
# =====================

# 1. Convert an if-elif chain to match-case
fruit = "apple"

match fruit:
    case "apple":
        print("Red")
    case "banana":
        print("Yellow")
    case "orange":
        print("Orange")
    case _:
        print("Unknown")

# 2. Create a HTTP status code handler
def handle_http(code):
    match code:
        case 200:
            return "OK"
        case 201:
            return "Created"
        case 204:
            return "No Content"
        case 301:
            return "Moved Permanently"
        case 400:
            return "Bad Request"
        case 401:
            return "Unauthorized"
        case 403:
            return "Forbidden"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return f"Unknown: {code}"

print(handle_http(404))

# 3. Match multiple values (yes, y, yeah)
def confirm(response):
    match response.lower():
        case "yes" | "y" | "yeah" | "yep":
            return "Confirmed"
        case "no" | "n" | "nope":
            return "Declined"
        case _:
            return "Invalid"

print(confirm("yeah"))

# 4. Use a guard to check a condition
grade = 95

match grade:
    case g if g >= 90:
        print("A - Excellent!")
    case g if g >= 80:
        print("B - Good!")
    case g if g >= 70:
        print("C - Average")
    case _:
        print("Need improvement")