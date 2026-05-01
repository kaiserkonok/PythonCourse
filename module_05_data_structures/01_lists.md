# Lists: Ordered Collections, Indexing, and Slicing

## Learning Objectives

- Create and use lists
- Access list elements by index
- Slice lists to get subsets

## What is a List?

A list is an **ordered collection** of items:
- Ordered: Items have a specific order
- Mutable: Can be changed
- Can hold different types

```python
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]
```

## Accessing Elements

Each item has an index (position):
```
fruits = ["apple", "banana", "cherry"]
          [0]       [1]       [2]
```

```python
fruits = ["apple", "banana", "cherry"]

print(fruits[0])   # apple (first)
print(fruits[1])   # banana (second)
print(fruits[2])   # cherry (third)
print(fruits[-1])  # cherry (last)
print(fruits[-2])  # banana (second to last)
```

## Modifying Lists

```python
fruits = ["apple", "banana", "cherry"]

# Change an item
fruits[0] = "orange"
print(fruits)  # ["orange", "banana", "cherry"]

# Add an item
fruits.append("date")
print(fruits)  # ["orange", "banana", "cherry", "date"]

# Insert at position
fruits.insert(1, "grape")
print(fruits)  # ["orange", "grape", "banana", "cherry", "date"]
```

## List Slicing

```python
numbers = [0, 1, 2, 3, 4, 5]

print(numbers[1:4])   # [1, 2, 3] (positions 1-3)
print(numbers[:3])    # [0, 1, 2] (start to 3)
print(numbers[3:])    # [3, 4, 5] (3 to end)
print(numbers[:])     # [0, 1, 2, 3, 4, 5] (all)
```

## Code Examples

```python
# Example 1: Create and access
colors = ["red", "green", "blue"]
print(colors[0])    # red
print(colors[-1])    # blue

# Example 2: Modify list
colors[0] = "yellow"
print(colors)        # ["yellow", "green", "blue"]

# Example 3: Add/remove items
colors.append("purple")
colors.append("orange")
print(colors)        # ["yellow", "green", "blue", "purple", "orange"]

colors.remove("green")  # Remove by value
print(colors)          # ["yellow", "blue", "purple", "orange"]

popped = colors.pop()   # Remove last
print(popped)          # orange
print(colors)          # ["yellow", "blue", "purple"]

# Example 4: List slicing
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[2:7])   # [2, 3, 4, 5, 6]
print(numbers[::2])    # [0, 2, 4, 6, 8] (every 2nd)
print(numbers[::-1])  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] (reverse)

# Example 5: List operations
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print(combined)         # [1, 2, 3, 4, 5, 6]

print([1] * 3)        # [1, 1, 1] (repeat)
```

## Key Takeaways

1. **Lists are ordered** - items have indexes
2. **Mutable** - can be modified in place
3. **Access by index** - [0], [-1]
4. **Slice with :** - [1:3], [:3], [3:]
5. **Methods** - append(), remove(), pop(), insert()

## Practice Exercise

1. Create a list of 5 fruits
2. Print the first and last fruit
3. Add a new fruit to the end
4. Print a slice of 3 fruits from the middle