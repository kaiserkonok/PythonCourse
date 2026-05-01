# Iteration with While Loops: Repeating Code Based on a Condition

## Learning Objectives

- Use while loops to repeat code
- Understand the loop condition
- Avoid infinite loops

## What is a While Loop?

A while loop **repeats code** as long as a condition is True:

```
while condition:
    # code to repeat
```

```python
count = 0

while count < 5:
    print(count)
    count += 1  # Important! Update the condition
```

## How While Loops Work

```
┌─────────────────┐
│  count = 0       │  ← Initialize
└────────┬────────┘
         │
         ▼
    ┌─────────┐
    │count<5? │──Yes──→ Print count, count += 1
    │         │  ↓ No
    │    No   │←──┘
    └────┬────┘
         │
         ▼
    Loop ends
```

## Infinite Loops (The Danger!)

Always ensure the condition eventually becomes False:

```python
# ❌ WRONG - Infinite loop!
while True:
    print("This never stops!")

# ✅ CORRECT - Condition changes
while True:
    print("Press q to quit")
    answer = input("Enter q: ")
    if answer == "q":
        break
```

## Code Examples

```python
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

# Example 3: Sum numbers until negative
total = 0

while True:
    num = int(input("Enter number (-1 to quit): "))
    if num < 0:
        break
    total += num
    print(f"Running total: {total}")

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

# Example 5: Only continue if valid
age = 0

while age < 1 or age > 120:
    age = int(input("Enter valid age: "))

print(f"You are {age} years old")
```

## Key Takeaways

1. **while** loops repeat while condition is True
2. **Always update** the variable in the condition
3. **Infinite loops** crash your program!
4. **break** exits the loop early
5. **Use for loops** when you know the iterations

## Practice Exercise

1. Print numbers 1 to 10 using while loop
2. Create a countdown from 10 to 1
3. Ask for input until user enters "quit"
4. Calculate sum of 0 to 100 using while loop