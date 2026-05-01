# Dunder Methods: Using "Magic Methods" to Customize Class Behavior

## Learning Objectives

- Understand dunder methods
- Implement common dunder methods
- Make classes more Pythonic

## What are Dunder Methods?

Dunder (double underscore) methods are **special methods** that start and end with `__`:

- Called automatically by Python
- Customize how objects behave
- Also called "magic methods"

```python
class Person:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f"Person: {self.name}"

person = Person("Alice")
print(person)  # Person: Alice
```

## Common Dunder Methods

| Method | Purpose |
|-------|---------|
| `__init__` | Initialize object |
| `__str__` | String representation |
| `__repr__` | Developer representation |
| `__len__` | Length |
| `__eq__` | Equal comparison |
| `__add__` | Addition (+) |

## Code Examples

```python
# Example 1: __str__ and __repr__
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name}, {self.age} years old"
    
    def __repr__(self):
        return f"Person('{self.name}', {self.age})"

p = Person("Alice", 25)
print(str(p))      # Alice, 25 years old
print(repr(p))     # Person('Alice', 25)

# Example 2: __len__
class Team:
    def __init__(self, members):
        self.members = members
    
    def __len__(self):
        return len(self.members)

team = Team(["Alice", "Bob", "Charlie"])
print(len(team))  # 3

# Example 3: __eq__
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

p1 = Point(1, 2)
p2 = Point(1, 2)
print(p1 == p2)  # True

# Example 4: __add__
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __str__(self):
        return f"({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2
print(v3)  # (4, 6)

# Example 5: __contains__
class Inventory:
    def __init__(self, items):
        self.items = items
    
    def __contains__(self, item):
        return item in self.items

inv = Inventory(["apple", "banana"])
print("apple" in inv)  # True
print("orange" in inv)  # False
```

## More Dunder Methods

```python
# __getitem__ - index access
def __getitem__(self, index):
    return self.items[index]

# __setitem__ - set value
def __setitem__(self, index, value):
    self.items[index] = value

# __iter__ - make iterable
def __iter__(self):
    return iter(self.items)

# __call__ - make callable
def __call__(self):
    return "Called!"
```

## When to Use Dunder Methods

- **Custom objects** - behave like built-ins
- **Debugging** - __repr__ for developers
- **Comparison** - __eq__, __lt__, etc.
- **Operators** - __add__, __sub__, etc.

## Key Takeaways

1. **__init__** - setup object
2. **__str__** - user-friendly string
3. **__repr__** - developer string
4. **__len__** - length
5. **__add__** - operator support
6. **Use sparingly** - when needed

## Practice Exercise

1. Create class with __str__ method
2. Create class with __len__ method
3. Create class with __add__ method
4. Implement __repr__ method