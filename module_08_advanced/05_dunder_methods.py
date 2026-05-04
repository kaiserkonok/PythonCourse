"""
Dunder Methods (Python's Magic Methods)
────────────────────────────────────────────────────────────────────────────
Code examples and practice exercises from the lesson.
────────────────────────────────────────────────────────────────────────────
"""

# Example 1 — `__str__` and `__repr__`
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} years old"

    def __repr__(self):
        return f"Person('{self.name}', {self.age})"

p = Person("Alice", 25)
print(p)          # Alice, 25 years old
print(repr(p))    # Person('Alice', 25)


# Example 2 — `__len__`
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def __len__(self):
        return len(self.items)

cart = ShoppingCart()
cart.add("Apple")
cart.add("Banana")
print(len(cart))  # 2


# Example 3 — `__eq__`
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y

p1 = Point(1, 2)
p2 = Point(1, 2)
p3 = Point(3, 4)

print(p1 == p2)  # True
print(p1 == p3)  # False


# Example 4 — `__add__`
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)  # Vector(4, 6)


# Example 5 — `__getitem__` and `__setitem__`
class MyList:
    def __init__(self, data):
        self._data = list(data)

    def __getitem__(self, index):
        return self._data[index]

    def __setitem__(self, index, value):
        self._data[index] = value

    def __len__(self):
        return len(self._data)

ml = MyList([10, 20, 30])
print(ml[0])    # 10
ml[1] = 99
print(ml[1])    # 99
print(len(ml))  # 3


# Example 6 — Making Objects Callable
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, x):
        return x * self.factor

double = Multiplier(2)
triple = Multiplier(3)

print(double(5))  # 10
print(triple(5))  # 15


# ═══════════════════════════════════════════════════════════════════════════════
# PRACTICE EXERCISE
# ═══════════════════════════════════════════════════════════════════════════════
# 1. Create a class with __str__ and __repr__
# 2. Implement __len__ for a custom collection
# 3. Add __eq__ to compare two objects
# 4. Implement __add__ for a custom math class
# ═══════════════════════════════════════════════════════════════════════════════

# 1-4. Complete Money class
class Money:
    def __init__(self, amount, currency="USD"):
        self.amount = amount
        self.currency = currency

    def __str__(self):
        return f"{self.amount} {self.currency}"

    def __repr__(self):
        return f"Money({self.amount}, '{self.currency}')"

    def __eq__(self, other):
        if not isinstance(other, Money):
            return False
        return self.amount == other.amount and self.currency == other.currency

    def __add__(self, other):
        if isinstance(other, Money) and self.currency == other.currency:
            return Money(self.amount + other.amount, self.currency)
        raise ValueError("Currencies must match")

    def __mul__(self, factor):
        return Money(self.amount * factor, self.currency)

    def __len__(self):
        return len(str(self.amount))

m1 = Money(100)
m2 = Money(50)

print(m1)               # 100 USD
print(repr(m1))         # Money(100, 'USD')
print(m1 == m2)         # False
print(m1 + m2)          # 150 USD
print(m1 * 3)           # 300 USD
print(len(m1))          # 3

# Try modifying it:
# - Make a class iterable with __iter__
class Team:
    def __init__(self, members):
        self.members = members

    def __iter__(self):
        return iter(self.members)

    def __len__(self):
        return len(self.members)

team = Team(["Alice", "Bob", "Charlie"])
for member in team:
    print(f"  {member}")
