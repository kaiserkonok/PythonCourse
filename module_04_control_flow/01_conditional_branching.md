# Conditional Branching: Mastering if, elif, and else

## Learning Objectives

- Use if statements to make decisions
- Chain conditions with elif
- Handle multiple cases with else

## The if Statement

The `if` statement lets your code make decisions:

```python
age = 18

if age >= 18:
    print("You can vote!")
```

## The Complete Structure

```
if condition:
    # runs if condition is True
elif condition2:
    # runs if first is False, second is True
else:
    # runs if all conditions are False
```

## if, elif, else Together

```python
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

print(f"Your grade: {grade}")  # B
```

## Multiple Conditions

```python
age = 25
has_license = True

# Multiple conditions with and/or
if age >= 18 and has_license:
    print("You can drive!")
else:
    print("You cannot drive")
```

## Code Examples

```python
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
```

## Key Takeaways

1. **if** checks a condition, runs if True
2. **elif** checks another condition if previous was False
3. **else** runs when no conditions matched
4. **Only one block executes** - first True condition runs
5. **elif is optional** - can have just if-else

## Practice Exercise

1. Create a grading system (A, B, C, D, F) using if-elif-else
2. Check if a number is positive, negative, or zero
3. Create a simple login check with username and password