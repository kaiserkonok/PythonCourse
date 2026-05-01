# Computer Architecture for Coders: How CPU and RAM Interact with Your Code

## Learning Objectives

- Understand the basic relationship between CPU, RAM, and your code
- Learn how data flows through a computer when code executes
- See why understanding memory matters for programming

## The CPU: The Brain of Your Computer

- **CPU** = Central Processing Unit
- Executes instructions (math, logic, data movement)
- Very fast, but can only work with data it has access to

```
┌─────────────────────────────────────┐
│           CPU                       │
│    ┌─────────────────────┐          │
│    │  Control Unit      │          │
│    │  Arithmetic Logic  │          │
│    │  Unit (ALU)        │          │
│    └─────────────────────┘          │
└─────────────────────────────────────┘
```

## RAM: Where Data Lives While Your Code Runs

- **RAM** = Random Access Memory
- Temporary storage (data lost when computer turns off)
- Stores both your code's instructions AND your data

```
┌─────────────────────────────────────┐
│              RAM                    │
│  ┌──────┬──────┬──────┬──────┐     │
│  │ 001 │ 002 │ 003 │ 004 │ ...│     │
│  │     │     │     │     │     │     │
│  │code │data │data │data │     │     │
│  └──────┴──────┴──────┴──────┘     │
│   Memory addresses (like house      │
│   numbers, but for data)            │
└─────────────────────────────────────┘
```

## How CPU and RAM Work Together

```
Step 1: LOAD
Your code tells CPU: "Get data from address 001"
┌──────┐     ┌──────┐
│ CPU  │ ←── │ RAM │
└──┬───┘     └──────┘
   │         
   ▼         
──────────    
Step 2: PROCESS
CPU executes: "Add 5 to this number"   
   │         
   ▼         
──────────    
Step 3: STORE
CPU tells RAM: "Put result at address 003"
┌──────┐     ┌──────┐
│ CPU  │ ──→ │ RAM │
└──────┘     └──────┘
```

## Python's Role in This Process

When you write Python code, you don't manage memory directly:

```python
x = 10          # Python decides where in RAM to store 10
y = x + 5       # CPU handles the math
print(y)        # Python retrieves and displays the result
```

| Without Python | With Python |
|---------------|-------------|
| You manage memory addresses | Python handles it automatically |
| You write raw instructions | You write readable code |
| More control, more complexity | Less control, less complexity |

## Code Examples

```python
# Example 1: Simple variable assignment
# Python stores "10" somewhere in RAM and labels it "x"
x = 10
print(x)

# Example 2: Multiple variables
# Each variable gets its own space in RAM
name = "Python"
version = 3.12
print(f"{name} {version}")

# Example 3: Operations in Python
a = 100
b = 50
result = a + b
print(result)  # Output: 150

# What happens internally:
# 1. CPU fetches a value from RAM (address of 'a')
# 2. CPU fetches b value from RAM (address of 'b')
# 3. CPU's ALU performs addition
# 4. CPU stores result back to RAM
```

## Key Takeaways

1. **CPU does the work** — executing instructions, doing math, making decisions
2. **RAM stores data temporarily** — both your code's instructions and your variables
3. **Python abstracts away the complexity** — you don't need to manage memory directly
4. **Variables are like labels** — they point to locations in RAM where data is stored

## Practice Exercise

Run this code and observe the output:

```python
x = 5
y = 10
z = x + y
print(f"x = {x}, y = {y}, z = {z}")
```

Think about: Where do x, y, and z live in RAM? What does the CPU do with these values?