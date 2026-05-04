"""
Encapsulation (Protecting Your Data)
────────────────────────────────────────────────────────────────────────────
Code examples and practice exercises from the lesson.
────────────────────────────────────────────────────────────────────────────
"""

# Example 1 — Public vs Private
class Account:
    def __init__(self, owner, balance):
        self.owner = owner      # Public
        self._balance = balance # Protected (internal)

acc = Account("Alice", 1000)
print(acc.owner)      # OK — public
print(acc._balance)   # Works, but shouldn't do it!


# Example 2 — Getters and Setters
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_age(self):
        return self._age

    def set_age(self, age):
        if 0 <= age <= 150:
            self._age = age
        else:
            print("Invalid age!")

p = Person("Alice", 25)
p.set_age(30)
print(p.get_age())  # 30
p.set_age(-5)       # Invalid age!


# Example 3 — @property Decorator
class PersonProperty:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if 0 <= value <= 150:
            self._age = value
        else:
            raise ValueError("Invalid age")

p2 = PersonProperty("Bob", 25)
print(p2.age)   # 25 (like attribute access)
p2.age = 30     # Calls setter
print(p2.age)   # 30


# Example 4 — Read-Only Properties
import math

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @property
    def area(self):
        return math.pi * self._radius ** 2

    @property
    def diameter(self):
        return self._radius * 2

c = Circle(5)
print(f"Radius: {c.radius}, Area: {c.area:.2f}, Diameter: {c.diameter}")
# c.radius = 10  ← AttributeError (no setter)


# Example 5 — Computed Properties
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self._celsius = (value - 32) * 5/9

t = Temperature(100)
print(f"{t._celsius}°C = {t.fahrenheit}°F")
t.fahrenheit = 212
print(f"{t._celsius:.1f}°C = {t.fahrenheit}°F")


# Example 6 — Data Hiding
class Database:
    def __init__(self):
        self.__password = "secret"  # Private (name-mangled)

    def get_password(self):
        # In real code, verify permissions here
        return self.__password

db = Database()
print(db.get_password())  # "secret"
# print(db.__password)    ← AttributeError


# ═══════════════════════════════════════════════════════════════════════════════
# PRACTICE EXERCISE
# ═══════════════════════════════════════════════════════════════════════════════
# 1. Create a class with a private attribute
# 2. Add a getter and setter with validation
# 3. Convert to use @property
# 4. Create a read-only computed property
# ═══════════════════════════════════════════════════════════════════════════════

class BankAccount:
    def __init__(self, owner, balance):
        self._owner = owner
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            raise ValueError("Deposit must be positive")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
        else:
            raise ValueError("Invalid withdrawal amount")

    def __str__(self):
        return f"{self._owner}: ${self._balance}"

account = BankAccount("Alice", 1000)
print(account)
account.deposit(500)
print(account)
account.withdraw(200)
print(account)

# Try modifying it:
# - Add transaction history
class TrackedAccount(BankAccount):
    def __init__(self, owner, balance):
        super().__init__(owner, balance)
        self._history = []

    def deposit(self, amount):
        super().deposit(amount)
        self._history.append(f"+${amount}")

    def withdraw(self, amount):
        super().withdraw(amount)
        self._history.append(f"-${amount}")

    @property
    def history(self):
        return self._history.copy()

tracked = TrackedAccount("Bob", 500)
tracked.deposit(100)
tracked.withdraw(50)
print(tracked.history)
