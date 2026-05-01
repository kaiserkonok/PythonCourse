# Environment Setup: Installing Python and PyCharm

## Learning Objectives

By the end of this lesson, you will be able to:

- Install Python 3.x on your machine
- Set up PyCharm Community Edition
- Create your first project and run your first script
- Understand why an IDE is worth your time

---

## Mental Model: Chef + Kitchen

Think of it this way:

- **Python** is the chef — it's the one who actually cooks (runs) your recipes
- **PyCharm** is the kitchen — it gives you the tools, workspace, and convenience to write good recipes
- **Your code** is the recipe — it tells the chef what to make

You *could* cook without a kitchen, but it would be messy. PyCharm makes writing code clean and organized.

---

## Why Use an IDE?

An IDE (Integrated Development Environment) is a program designed specifically for writing code. Here's what PyCharm gives you out of the box:

| Feature | What It Does | Why It Matters |
|---------|-------------|---------------|
| **Syntax highlighting** | Colors your code | Makes it readable at a glance |
| **Auto-complete** | Suggests code as you type | Saves time, prevents typos |
| **Error detection** | Highlights mistakes before you run | Catches bugs early |
| **One-click run** | Execute your script with one click | No terminal commands needed |
| **Debugging** | Step through code line by line | Find and fix bugs fast |

---

## Step 1: Download and Install Python

Python is the engine that actually runs your code.

1. Go to **[python.org](https://python.org)**
2. Hover over **Downloads**
3. Click the latest version for your OS (Windows / macOS / Linux)
4. Run the installer

### ⚠️ Critical Step for Windows Users

During installation, you will see a checkbox:

```
☐  Add python.exe to PATH
```

**You MUST check this box.** Without it, you won't be able to run Python from the terminal.

```
✅ Add Python 3.12 to PATH
   This makes Python accessible from anywhere on your computer.
```

### Verify Python is Installed

Open a terminal (or Command Prompt on Windows) and type:

```bash
python --version
```

You should see something like:

```
Python 3.12.x
```

If you see that — you're good to go. If not, try reinstalling and make sure you checked the "Add to PATH" box.

---

## Step 2: Download and Install PyCharm

PyCharm is the IDE (code editor) you'll use to write Python.

1. Go to **[jetbrains.com/pycharm](https://www.jetbrains.com/pycharm/)**
2. Click **Download** under **Community** (it's free!)
3. Run the installer
4. Follow the default settings — you don't need to change anything

### Community vs. Professional

| Edition | Price | Features |
|---------|-------|----------|
| **Community** | Free | Everything you need for this course |
| **Professional** | $199/year | Extra tools for web development |

For this course, **Community is perfect**. You don't need Professional.

---

## Step 3: Create Your First Project

1. Open PyCharm
2. Click **New Project**
3. Name it: `my_first_project`
4. Leave the Python interpreter as default (PyCharm auto-detects it)
5. Click **Create**

### Inside Your Project

```
my_first_project/
├── 📁 .idea/              ← PyCharm settings (ignore this)
├── 📄 hello_world.py      ← Your first Python file
└── 📄 other_file.py       ← More files you'll create
```

### Create Your First File

1. **Right-click** on the project folder in the left panel
2. Select **New → Python File**
3. Name it: `hello_world`
4. Write your code and run it!

---

## Step 4: Run Your First Script

Write this in your `hello_world.py` file:

```python
print("Hello, World!")
```

To run it:

- **Right-click** anywhere in the editor → **Run 'hello_world'**
- OR press `Ctrl+Shift+F10` (Windows/Linux) or `Cmd+Shift+R` (Mac)
- OR click the green ▶ button in the top-right corner

You should see:

```
Hello, World!
```

---

## Common Mistakes

```
❌ Not checking "Add to PATH" during Python installation
   Fix: Reinstall Python and check the box.

❌ Installing PyCharm Professional instead of Community
   Fix: Uninstall and download the free Community edition.

❌ Not knowing where to run code
   Fix: Right-click in the editor → Run, or use the green ▶ button.

❌ Trying to write code in Notepad/TextEdit
   Fix: Use PyCharm. It highlights errors and auto-completes.
```

---

## Code Examples

### Example 1 — Your First Program

```python
# This is the simplest Python program
print("Hello, World!")
# Output: Hello, World!
```

### Example 2 — Calculate Something

```python
# Python does the math for you
result = 2 + 2
print(f"2 + 2 = {result}")
# Output: 2 + 2 = 4
```

### Example 3 — Use Variables

```python
# Store a value and print it
message = "Python is fun!"
print(message)
# Output: Python is fun!
```

### Example 4 — Multiple Prints

```python
# Each print() goes on a new line
print("Line 1")
print("Line 2")
print("Line 3")
# Output:
# Line 1
# Line 2
# Line 3
```

---

## PyCharm Shortcuts Cheat Sheet

| Action | Windows / Linux | Mac |
|-------|-----------------|-----|
| Run code | `Ctrl+Shift+F10` | `Cmd+Shift+R` |
| Save file | `Ctrl+S` | `Cmd+S` |
| Comment line | `Ctrl+/` | `Cmd+/` |
| Format code | `Ctrl+Alt+L` | `Cmd+Opt+L` |
| Find and replace | `Ctrl+R` | `Cmd+R` |
| Go to line | `Ctrl+G` | `Cmd+G` |

---

## Practice Exercise

1. Open PyCharm
2. Create a new Python file
3. Write code that prints your name and favorite color
4. Run it!

**Expected output:** `My name is [Name] and I like [Color]`

---

## Key Takeaways

- **Python** is the engine — it executes your code
- **PyCharm** is the IDE — it makes writing code easier
- **Always check "Add to PATH"** during Python installation
- **Run code** by right-clicking → Run or using the green ▶ button
- **Start small** — your first program should be simple, like printing "Hello!"

---

## Further Reading

- [Python Installation Guide — Official Docs](https://docs.python.org/3/using/index.html)
- [PyCharm Quick Start Guide](https://www.jetbrains.com/pycharm/guide/)
- [VS Code Alternative](https://code.visualstudio.com/) — If you prefer a lighter editor