# Code examples from "Dunder Methods" lesson

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
print("str:", str(p))      # Alice, 25 years old
print("repr:", repr(p))     # Person('Alice', 25)

print("---")

# Example 2: __len__
class Team:
    def __init__(self, members):
        self.members = members
    
    def __len__(self):
        return len(self.members)

team = Team(["Alice", "Bob", "Charlie"])
print("Team size:", len(team))  # 3

print("---")

# Example 3: __eq__
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __repr__(self):
        return f"Point({self.x}, {self.y})"

p1 = Point(1, 2)
p2 = Point(1, 2)
print("p1 == p2:", p1 == p2)  # True
print("p1:", repr(p1))

print("---")

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
print("v1 + v2:", v3)  # (4, 6)

print("---")

# Example 5: __contains__
class Inventory:
    def __init__(self, items):
        self.items = items
    
    def __contains__(self, item):
        return item in self.items
    
    def __len__(self):
        return len(self.items)

inv = Inventory(["apple", "banana", "cherry"])
print("'apple' in inv:", "apple" in inv)  # True
print("'orange' in inv:", "orange" in inv)  # False
print("Inventory len:", len(inv))  # 3

print("---")

# Example 6: __call__
class Counter:
    def __init__(self):
        self.count = 0
    
    def __call__(self):
        self.count += 1
        return self.count

c = Counter()
print("First call:", c())   # 1
print("Second call:", c())  # 2
print("Third call:", c())   # 3


# =====================
# PRACTICE EXERCISE
# =====================

# 1. Create class with __str__ method
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def __str__(self):
        return f"'{self.title}' by {self.author}"

book = Book("1984", "George Orwell")
print(book)  # '1984' by George Orwell

# 2. Create class with __len__ method
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def __len__(self):
        return len(self.items)

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(f"Stack length: {len(stack)}")  # 3

# 3. Create class with __add__ method
class Money:
    def __init__(self, amount):
        self.amount = amount
    
    def __add__(self, other):
        return Money(self.amount + other.amount)
    
    def __str__(self):
        return f"${self.amount}"
    
    def __repr__(self):
        return f"Money({self.amount})"

m1 = Money(10)
m2 = Money(20)
m3 = m1 + m2
print(f"Total: {m3}")  # $30

# 4. Implement __repr__ method
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    
    def __repr__(self):
        return f"Player(name='{self.name}', score={self.score})"

player = Player("Alice", 100)
print(repr(player))  # Player(name='Alice', score=100)