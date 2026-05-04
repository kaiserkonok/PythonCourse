# 📁 File Handling: Reading & Writing Files

<p align="center">
  <img src="https://img.shields.io/badge/open-Read%2FWrite-blue?style=flat-square" alt="open">
  <img src="https://img.shields.io/badge/with-Auto%20Close-green?style=flat-square" alt="with">
  <img src="https://img.shields.io/badge/IO-Persistent%20Data-orange?style=flat-square" alt="IO">
</p>

> ### 💡 File handling is how your program talks to the outside world — reading data from files and writing results back.
> Learn how to open, read, write, and manage files safely.

---

## 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- ✅ Open and close files safely using `with`
- ✅ Read and write text files
- ✅ Understand file modes: `r`, `w`, `a`, `x`
- ✅ Handle file errors gracefully

---

## 🧠 Mental Model: A Notebook

File handling is like using a **notebook**:

```
📓 Open notebook → Read pages → Write new pages → Close notebook
   (open)          (read)         (write)           (close)
```

The `with` statement automatically closes the notebook when you're done.

---

## 📖 File Modes

| Mode | What it does | If file exists | If file missing |
|------|-------------|----------------|-----------------|
| `r` | Read | Opens it | ❌ Error |
| `w` | Write (overwrite) | Erases & opens | Creates new |
| `a` | Append | Opens at end | Creates new |
| `x` | Exclusive create | ❌ Error | Creates new |

---

## 📊 Reading Files

```python
# Read entire file
with open("file.txt", "r") as f:
    content = f.read()

# Read line by line
with open("file.txt", "r") as f:
    for line in f:
        print(line.strip())

# Read all lines into a list
with open("file.txt", "r") as f:
    lines = f.readlines()
```

---

## ⚠️ Common Mistakes

```
❌ Forgetting to close files
   f = open("file.txt")
   data = f.read()
   # f.close() missing → Resource leak!
   with open("file.txt") as f:  ← Auto-closes!

❌ Using wrong mode
   f = open("file.txt", "w")  ← Erases existing content!
   f = open("file.txt", "a")  ← Appends safely

❌ Not handling missing files
   with open("missing.txt") as f:  ← FileNotFoundError
   try:
       with open("missing.txt") as f:
           ...
   except FileNotFoundError:
       print("File not found")

❌ Encoding issues
   with open("file.txt", encoding="utf-8") as f:  ← Always specify encoding!
```

---

## 💻 Code Examples

### 📌 Example 1 — Writing to a File

```python
with open("output.txt", "w") as f:
    f.write("Hello, World!\n")
    f.write("Second line\n")
```

### 📌 Example 2 — Reading a File

```python
with open("output.txt", "r") as f:
    content = f.read()
    print(content)
```

### 📌 Example 3 — Reading Line by Line

```python
# Create a sample file first
with open("lines.txt", "w") as f:
    f.write("Line 1\nLine 2\nLine 3\n")

# Read line by line
with open("lines.txt", "r") as f:
    for line in f:
        print(line.strip())
```

### 📌 Example 4 — Appending to a File

```python
with open("log.txt", "a") as f:
    f.write("New log entry\n")
```

### 📌 Example 5 — Working with CSV-like Data

```python
# Write CSV-like data
with open("data.txt", "w") as f:
    f.write("Name,Age,City\n")
    f.write("Alice,25,NY\n")
    f.write("Bob,30,LA\n")

# Read and parse
with open("data.txt", "r") as f:
    for line in f:
        parts = line.strip().split(",")
        if len(parts) == 3:
            print(f"{parts[0]} is {parts[1]}, from {parts[2]}")
```

### 📌 Example 6 — Error Handling

```python
try:
    with open("missing.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("File not found!")
except PermissionError:
    print("No permission to read!")
except Exception as e:
    print(f"Unexpected error: {e}")
```

---

## 🧪 Practice Exercise

1. Create a file and write a few lines to it
2. Read the file back and print each line
3. Append a new line to the file
4. Handle the case where the file doesn't exist

---

## 📋 Key Takeaways

| Concept | Takeaway |
|---------|----------|
| 📂 **`with open()`** | Always use `with` — auto-closes files |
| 📝 **Modes** | `r` (read), `w` (write), `a` (append) |
| 📖 **Read** | `read()` (all), `readline()` (one), `readlines()` (list) |
| ✍️ **Write** | `write()` (string), `writelines()` (list) |
| 🛡️ **Errors** | Handle `FileNotFoundError` gracefully |

---

## 🔗 Further Reading

- 📖 [Input and Output — Official Docs](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
- 🌟 [File Handling — Real Python](https://realpython.com/read-write-files-python/)
- 🔧 [Pathlib — Modern File Paths](https://docs.python.org/3/library/pathlib.html)