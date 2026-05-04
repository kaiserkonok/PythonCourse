# 🎛️ Loop Control: `break`, `continue`, and `else`

<p align="center">
  <img src="https://img.shields.io/badge/break-Exit%20Loop-red?style=flat-square" alt="break">
  <img src="https://img.shields.io/badge/continue-Skip-orange?style=flat-square" alt="continue">
  <img src="https://img.shields.io/badge/else-After%20Loop-green?style=flat-square" alt="else">
</p>

> ### 💡 Loop control statements are the steering wheel — they let you exit early, skip ahead, or detect when a loop finishes normally.
> Learn how to fine-tune your loops with `break`, `continue`, and `else`.

---

## 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- ✅ Use `break` to exit a loop early
- ✅ Use `continue` to skip to the next iteration
- ✅ Use the loop `else` clause to detect normal completion

---

## 🧠 Mental Model: Traffic Control

Think of loop controls like **traffic signals**:

| Control | Signal | What it does |
|---------|--------|--------------|
| `break` | 🛑 Red Light | Stop immediately — exit the loop |
| `continue` | 🟡 Yellow Light | Skip this one — go to next iteration |
| `else` | ✅ Green Light | Loop finished normally — run cleanup |

---

## 📖 The Controls

### 🔴 `break` — Exit Immediately

```python
for i in range(10):
    if i == 5:
        break
    print(i)  # 0, 1, 2, 3, 4
```

> 💡 Use `break` when you found what you're looking for and don't need to continue.

### 🟡 `continue` — Skip to Next

```python
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)  # 1, 3, 5, 7, 9 (skips evens)
```

> 💡 Use `continue` to skip unwanted iterations without exiting the loop.

### ✅ `else` — After Normal Completion

```python
for item in items:
    if item == target:
        print("Found it!")
        break
else:
    print("Not found")  # Only runs if loop didn't break!
```

> 💡 The `else` block runs only if the loop finished **without** hitting `break`.

---

## 📊 When to Use Each

| Scenario | Control | Why |
|----------|---------|-----|
| Search and found | `break` | Stop searching |
| Filter out bad data | `continue` | Skip invalid items |
| Verify all items | `else` | Confirm no breaks occurred |
| User quit early | `break` | Exit gracefully |
| Skip header row | `continue` | Process data only |

---

## ⚠️ Common Mistakes

```
❌ Confusing loop `else` with `if/else`
   for x in items:
       if condition:
           break
   else:
       # This runs if loop completed WITHOUT break
       # NOT "if condition was False"

❌ Using break when continue is needed
   for x in data:
       if x is invalid:
           break      ← Stops entire loop!
           continue   ← Skips just this item

❌ Forgetting break in search loops
   for item in items:
       if item == target:
           print("Found")
           # Missing break → keeps checking rest of items

❌ Using else without break
   for x in items:
       process(x)
   else:
       # Always runs — same as putting code after the loop
       # Only useful when combined with break
```

---

## 💻 Code Examples

### 📌 Example 1 — `break` in a For Loop

```python
# Search for a number
target = 7
numbers = [1, 3, 5, 7, 9, 11]

for num in numbers:
    if num == target:
        print(f"Found {target}!")
        break
    print(f"Checking {num}...")
```

### 📌 Example 2 — `break` in a While Loop

```python
# Keep asking until user enters "quit"
while True:
    command = input("Enter command (or 'quit' to exit): ")
    if command == "quit":
        print("Goodbye!")
        break
    print(f"Running: {command}")
```

### 📌 Example 3 — `continue` in Action

```python
# Process only odd numbers
for i in range(10):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(f"Processing {i}")
```

### 📌 Example 4 — `continue` to Skip Errors

```python
# Process data, skip invalid entries
data = [10, 0, 20, "bad", 30]

for item in data:
    try:
        result = 100 / item
        print(f"100 / {item} = {result}")
    except (ZeroDivisionError, TypeError):
        print(f"Skipping {item} (invalid)")
        continue
```

### 📌 Example 5 — `else` with `break`

```python
# Check if a number is prime
number = 17

for i in range(2, number):
    if number % i == 0:
        print(f"{number} is not prime (divisible by {i})")
        break
else:
    # Only runs if loop didn't break
    print(f"{number} is prime!")
```

### 📌 Example 6 — Combining All Three

```python
# Process a list, skip negatives, stop at 999
numbers = [5, -2, 10, -8, 15, 999, 20]

for num in numbers:
    if num == 999:
        print("Found sentinel value, stopping!")
        break
    if num < 0:
        print(f"Skipping negative: {num}")
        continue
    print(f"Processing: {num}")
else:
    print("All numbers processed (no 999 found)")
```

---

## 🧪 Practice Exercise

1. Use `break` to stop a loop when you find a specific number
2. Use `continue` to skip numbers divisible by 3
3. Use `else` to detect if a search failed
4. Combine `break` and `continue` in one loop

---

## 📋 Key Takeaways

| Concept | Takeaway |
|---------|----------|
| 🛑 **`break`** | Exits the loop immediately — no more iterations |
| 🟡 **`continue`** | Skips to next iteration — rest of loop body is skipped |
| ✅ **`else`** | Runs when loop finishes normally (no `break`) |
| 🔍 **Search pattern** | `for/break/else` is idiomatic for "find or not found" |
| ⚠️ **Nested loops** | `break` only exits the innermost loop |

---

## 🔗 Further Reading

- 📖 [Break and Continue — Official Docs](https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops)
- 🌟 [Python Loop Else — Real Python](https://realpython.com/python-loop-else/)
- 🧠 [Control Flow — W3Schools](https://www.w3schools.com/python/python_while_loops.asp)