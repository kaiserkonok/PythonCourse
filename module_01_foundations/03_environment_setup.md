# Environment Setup: Setting Up PyCharm and Python

## Learning Objectives

- Download and install Python 3.x
- Install PyCharm IDE (Community Edition)
- Create your first Python project
- Run your first Python script

## Why Use an IDE?

| Tool | Purpose |
|-----|---------|
| **Python** | The language runtime that executes your code |
| **PyCharm** | An Integrated Development Environment - makes writing code easier |
| **Together** | You write code in PyCharm, Python runs it |

### What PyCharm Gives You:
- Syntax highlighting (colors for code)
- Auto-complete (suggests code as you type)
- Error detection (highlights mistakes before you run)
- Debugging tools (find bugs step by step)

## Step-by-Step Setup

### Step 1: Download Python

1. Go to: **python.org**
2. Click **Downloads**
3. Select your operating system (Windows/Mac/Linux)
4. Download **Python 3.x** (latest version)
5. Run the installer

**Important:** Check "Add Python to PATH" during installation!

```
✅ Add Python 3.12 to PATH
   (This makes Python accessible from command line)
```

### Step 2: Download PyCharm

1. Go to: **jetbrains.com/pycharm**
2. Download **PyCharm Community** (it's free!)
3. Run the installer

### Step 3: Create Your First Project

```
1. Open PyCharm
2. Click "New Project"
3. Name it "my_first_project"
4. Choose Python interpreter (PyCharm detects it automatically)
5. Click "Create"
```

## Your First Python Script

Inside your project:

```python
# 1. Right-click on the project folder
# 2. Select New → Python File
# 3. Name it "hello_world"

# 4. Write this code:
print("Hello, World!")

# 5. Right-click and select "Run 'hello_world'"
#    OR press Ctrl+Shift+F10 (Windows) / Cmd+Shift+R (Mac)
```

## Code Examples

```python
# Example 1: Your first program
print("Hello, World!")

# Example 2: Calculate something
result = 2 + 2
print(f"2 + 2 = {result}")

# Example 3: Use variables
message = "Python is fun!"
print(message)

# Example 4: Multiple prints
print("Line 1")
print("Line 2")
print("Line 3")
```

## PyCharm Shortcuts Cheat Sheet

| Action | Windows | Mac |
|-------|---------|-----|
| Run code | Ctrl+Shift+F10 | Cmd+Shift+R |
| Open file | Ctrl+N | Cmd+N |
| Save file | Ctrl+S | Cmd+S |
| Comment line | Ctrl+/ | Cmd+/ |
| Format code | Ctrl+Alt+L | Cmd+Opt+L |

## Key Takeaways

1. **Python** is the language runtime - it executes your code
2. **PyCharm** is the IDE - it makes writing code easier and more enjoyable
3. **"Run"** executes your script - you'll use this constantly!
4. **Practice running code** - every line you learn should be tested

## Practice Exercise

1. Create a new project in PyCharm
2. Create a Python file named "test"
3. Write code that prints your name and favorite color
4. Run it!

Example: "My name is [Name] and I like [Color]"