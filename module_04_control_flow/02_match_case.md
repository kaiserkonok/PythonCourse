# Match-Case (Structural Pattern Matching)

## Learning Objectives

- Use the match-case statement (Python 3.10+)
- Understand pattern matching vs traditional if-elif
- Match different types of patterns

## What is Match-Case?

Match-case is a **modern switch statement** for Python (Python 3.10+).

- Cleaner than multiple if-elif
- Supports complex patterns
- More readable for multi-way conditionals

## Basic Match-Case

```python
day = "Monday"

match day:
    case "Monday":
        print("Start of week")
    case "Friday":
        print("End of week")
    case "Saturday" | "Sunday":  # Multiple values with |
        print("Weekend!")
    case _:
        print("Just another day")
```

## Match vs if-elif

| if-elif | match-case |
|---------|----------|
| Older syntax | Python 3.10+ |
| Good for simple equality | Good for complex patterns |
| More verbose | Cleaner syntax |

## Matching Different Patterns

```python
# Simple match
status = 200

match status:
    case 200:
        print("OK")
    case 404:
        print("Not Found")
    case 500:
        print("Server Error")
    case _:
        print("Unknown")
```

## Code Examples

```python
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
```

## Key Takeaways

1. **match-case** is Python 3.10+
2. **case _** is the default (like else)
3. **|** matches multiple values
4. **Guards** add conditions with if
5. **Cleaner than if-elif** for multi-way branches

## Practice Exercise

1. Convert an if-elif chain to match-case
2. Create a HTTP status code handler
3. Match multiple values (yes, y, yeah)
4. Use a guard to check a condition