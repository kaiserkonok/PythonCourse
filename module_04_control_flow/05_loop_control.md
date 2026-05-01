# Loop Control: Advanced Use of break, continue, and pass

## Learning Objectives

- Use break to exit loops early
- Use continue to skip iterations
- Use pass as a placeholder

## The Three Control Statements

| Statement | What it does |
|-----------|-------------|
| break | Exit the loop completely |
| continue | Skip this iteration |
| pass | Do nothing (placeholder) |

## Using break

```python
# Exit loop when condition is met
for i in range(10):
    if i == 5:
        break  # Stop at 5
    print(i)
# Output: 0 1 2 3 4
```

## Using continue

```python
# Skip certain values
for i in range(5):
    if i == 2:
        continue  # Skip 2
    print(i)
# Output: 0 1 3 4 (skips 2)
```

## Using pass

```python
# pass does nothing - placeholder for future code
for i in range(5):
    pass  # Will implement later

print("Done")
```

## Common Patterns

```python
# Find first match, then stop
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num > 3:
        print(f"Found: {num}")
        break

# Skip even numbers
for i in range(10):
    if i % 2 == 0:
        continue
    print(f"Odd: {i}")

# Empty function body (can't have empty def)
def my_function():
    pass  # TODO: implement later
```

## Code Examples

```python
# Example 1: break - find first match
fruits = ["apple", "banana", "cherry", "date"]

for fruit in fruits:
    if fruit == "cherry":
        print(f"Found {fruit}!")
        break
    else:
        print(f"Not {fruit}")

# Example 2: continue - skip even numbers
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)  # 1 3 5 7 9

# Example 3: pass - placeholder
class MyClass:
    pass  # Will add methods later

# Example 4: break in while loop
count = 0

while True:
    print(count)
    count += 1
    if count >= 5:
        break

# Example 5: continue in while loop
count = 0

while count < 5:
    count += 1
    if count == 3:
        continue
    print(count)  # 1 2 4 5 (skips 3)
```

## Summary: When to Use

- **break**: Exit loop when found what you're looking for
- **continue**: Skip unwanted items
- **pass**: Need statement but no action yet

## Key Takeaways

1. **break** exits the loop entirely
2. **continue** skips to next iteration
3. **pass** is a placeholder
4. Use break when searching for something
5. Use continue to filter items

## Practice Exercise

1. Find the first number divisible by 7 from 1-50
2. Print all numbers 1-10 except multiples of 3
3. Use pass in a for loop that prints nothing
4. Combine break and continue in one loop