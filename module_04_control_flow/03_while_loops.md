# 🔁 While Loops: Repeating Until Done

<p align="center">
  <img src="https://img.shields.io/badge/while-Loop-blue?style=flat-square" alt="while">
  <img src="img.shields.io/badge/Condition-Check-green?style=flat-square" alt="Condition">
  <img src="https://img.shields.io/badge/Danger-Infinite%20Loops-red?style=flat-square" alt="Infinite">
</p>

> ### 💡 A `while` loop keeps going until a condition becomes False. Like a microwave timer — it runs until it hits zero.
> Learn how to repeat code based on conditions.

---

## 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- ✅ Use `while` loops to repeat code until a condition is met
- ✅ Avoid infinite loops by updating the condition variable
- ✅ Use `break` and `continue` to control loop flow

---

## 🧠 Mental Model: A Microwave Timer

A `while` loop is like a **microwave**:

```
Start:  2:00 remaining → Run microwave
Check:  1:30 remaining → Run microwave
Check:  0:30 remaining → Run microwave
Check:  0:00 remaining → STOP
```

It keeps checking the condition and running as long as it's `True`.

---

## 📖 Basic Syntax

```python
while condition:
    # Run this code
    # Update condition eventually!
```

### Key Rules

1. **Condition is checked first** — before each iteration
2. **Loop runs while True** — stops when condition becomes `False`
3. **Must update condition** — or you get an infinite loop!

---

## 📊 Examples at a Glance

| Pattern | Code |
|---------|------|
| Counting | `while i < 5: i += 1` |
| User Input | `while not valid: ...` |
| Infinite Loop | `while True: ...` (use `break` to exit) |
| With `else` | Runs when loop finishes normally |

---

## ⚠️ Common Mistakes

```
❌ Forgetting to update the condition
   i = 0
   while i < 5:
       print(i)
   # i never changes → INFINITE LOOP!

❌ Off-by-one errors
   i = 1
   while i <= 5:
       print(i)
       i += 1
   # Prints 1, 2, 3, 4, 5 (5 iterations)
   # Use < 5 for 1, 2, 3, 4 (4 iterations)

❌ Infinite loops from bad logic
   while x > 0:
       x += 1  # x grows forever → never stops!

❌ Using while when for is better
   i = 0
   while i < len(items):    ← Verbose
       print(items[i])
       i += 1

   for item in items:       ← Cleaner
       print(item)
```

---

## 💻 Code Examples

### 📌 Example 1 — Basic While Loop

```python
count = 0

while count < 5:
    print(f"Count: {count}")
    count += 1  # Don't forget this!

print("Done!")
```

### 📌 Example 2 — User Input Validation

```python
while True:
    age = input("Enter your age (positive number): ")
    if age.isdigit() and int(age) > 0:
        age = int(age)
        break
    print("Invalid input. Try again.")

print(f"Age: {age}")
```

### 📌 Example 3 — Countdown

```python
seconds = 5

while seconds > 0:
    print(f"{seconds}...")
    seconds -= 1

print("Go! 🚀")
```

### 📌 Example 4 — `break` and `continue`

```python
# break — exit the loop early
i = 0
while i < 10:
    i += 1
    if i == 5:
        break
    print(i)  # 1, 2, 3, 4

# continue — skip to next iteration
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)  # 1, 2, 4, 5 (skips 3)
```

### 📌 Example 5 — While with `else`

```python
# The `else` block runs when the loop finishes normally
# (not when broken with `break`)

n = 3

while n > 0:
    print(f"Countdown: {n}")
    n -= 1
else:
    print("Liftoff! 🚀")
```

### 📌 Example 6 — Nested While Loops

```python
# Multiplication table
row = 1

while row <= 3:
    col = 1
    while col <= 3:
        print(f"{row} x {col} = {row * col}")
        col += 1
    print("---")
    row += 1
```

---

## 🧪 Practice Exercise

1. Use a `while` loop to print numbers 1 to 10
2. Create a loop that asks for a number until the user enters 0
3. Use `break` to stop a loop when a condition is met
4. Use `continue` to skip even numbers in a loop

---

## 📋 Key Takeaways

| Concept | Takeaway |
|---------|----------|
| 🔁 **`while`** | Repeats while condition is `True` |
| 🛑 **`break`** | Exits the loop immediately |
| ⏭️ **`continue`** | Skips to next iteration |
| 🔄 **`else`** | Runs when loop finishes normally |
| ⚠️ **Infinite loops** | Always update the condition variable! |

---

## 🔗 Further Reading

- 📖 [While Statements — Official Docs](https://docs.python.org/3/reference/compound_stmts.html#the-while-statement)
- 🛑 [Break and Continue — docs](https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops)
- 🧠 [Python While Loops — W3Schools](https://www.w3schools.com/python/python_while_loops.asp)