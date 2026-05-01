# File Handling: Interacting with the Local File System

## Learning Objectives

- Read from files
- Write to files
- Handle file operations safely

## Reading Files

```python
# Read entire file
with open("file.txt", "r") as file:
    content = file.read()
    print(content)
```

## Writing Files

```python
# Write to file
with open("file.txt", "w") as file:
    file.write("Hello, World!")
```

## File Modes

| Mode | Description |
|------|-------------|
| "r" | Read (default) |
| "w" | Write (overwrites) |
| "a" | Append |
| "r+" | Read and write |

## Code Examples

```python
# Example 1: Read entire file
# with open("example.txt", "r") as file:
#     content = file.read()
#     print(content)

# Example 2: Read line by line
# with open("example.txt", "r") as file:
#     for line in file:
#         print(line, end="")

# Example 3: Write to file
# with open("output.txt", "w") as file:
#     file.write("Line 1\n")
#     file.write("Line 2\n")

# Example 4: Append to file
# with open("log.txt", "a") as file:
#     file.write("New entry\n")

# Example 5: Read all lines into list
# with open("example.txt", "r") as file:
#     lines = file.readlines()
#     for i, line in enumerate(lines):
#         print(f"{i}: {line}", end="")
```

## Safe File Handling

```python
import os

# Check if file exists
if os.path.exists("file.txt"):
    with open("file.txt", "r") as file:
        content = file.read()
else:
    print("File not found")
```

## JSON Files

```python
import json

# Write JSON
data = {"name": "Alice", "age": 25}
with open("data.json", "w") as file:
    json.dump(data, file)

# Read JSON
with open("data.json", "r") as file:
    data = json.load(file)
    print(data)
```

## Key Takeaways

1. **with open()** - safe file handling (auto closes)
2. **"r"** - read mode
3. **"w"** - write mode (overwrites)
4. **"a"** - append mode
5. **json** - for structured data

## Practice Exercise

1. Write text to a file
2. Read the file back
3. Append more text
4. Handle missing file gracefully