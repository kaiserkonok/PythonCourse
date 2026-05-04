"""
Polymorphism (Many Forms, One Interface)
────────────────────────────────────────────────────────────────────────────
Code examples and practice exercises from the lesson.
────────────────────────────────────────────────────────────────────────────
"""

# Example 1 — Basic Polymorphism
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class Bird:
    def speak(self):
        return "Tweet!"

# Works with any object that has speak()
for animal in [Dog(), Cat(), Bird()]:
    print(animal.speak())


# Example 2 — Function Polymorphism
def make_it_speak(animal):
    """Works with ANY object that has speak()."""
    print(animal.speak())

make_it_speak(Dog())   # Woof!
make_it_speak(Cat())   # Meow!
make_it_speak(Bird())  # Tweet!


# Example 3 — Inheritance Polymorphism
class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r ** 2

shapes = [Rectangle(5, 3), Circle(4), Rectangle(2, 6)]
for shape in shapes:
    print(f"Area: {shape.area()}")


# Example 4 — Duck Typing
class File:
    def process(self):
        print("Processing file...")

class Email:
    def process(self):
        print("Processing email...")

def process(item):
    """Works with anything that has process() method."""
    item.process()

process(File())   # Processing file...
process(Email())  # Processing email...


# Example 5 — Operator Overloading
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
print(v1 + v2)  # (4, 6)


# Example 6 — len() Polymorphism
# Built-in functions use polymorphism too!
print(len("hello"))        # 5 (string)
print(len([1, 2, 3]))      # 3 (list)
print(len({"a": 1, "b": 2}))  # 2 (dict)

# All work because they implement __len__


# ═══════════════════════════════════════════════════════════════════════════════
# PRACTICE EXERCISE
# ═══════════════════════════════════════════════════════════════════════════════
# 1. Create two classes with the same method name but different behavior
# 2. Write a function that accepts either class
# 3. Use + operator on a custom class
# 4. Create a list of different objects and call the same method on each
# ═══════════════════════════════════════════════════════════════════════════════

# 1-2. Payment classes
class CreditCard:
    def pay(self, amount):
        print(f"Paid ${amount} via Credit Card")

class PayPal:
    def pay(self, amount):
        print(f"Paid ${amount} via PayPal")

def checkout(payment_method, amount):
    payment_method.pay(amount)

checkout(CreditCard(), 100)
checkout(PayPal(), 50)

# 3. Custom + operator
class Money:
    def __init__(self, amount, currency="USD"):
        self.amount = amount
        self.currency = currency

    def __add__(self, other):
        if self.currency == other.currency:
            return Money(self.amount + other.amount, self.currency)
        raise ValueError("Currencies must match")

    def __str__(self):
        return f"{self.amount} {self.currency}"

m1 = Money(50)
m2 = Money(30)
print(m1 + m2)  # 80 USD

# 4. List of different objects
class Notifier:
    def send(self):
        print("Sending...")

class Email2:
    def send(self):
        print("Sending email...")

class SMS:
    def send(self):
        print("Sending SMS...")

notifiers = [Notifier(), Email2(), SMS()]
for n in notifiers:
    n.send()

# Try modifying it:
# - Create a generic function that calculates "value" for any object
class Product:
    def __init__(self, price, tax=0.08):
        self.price = price
        self.tax = tax

    def total(self):
        return self.price * (1 + self.tax)

class Service:
    def __init__(self, hourly_rate, hours):
        self.hourly_rate = hourly_rate
        self.hours = hours

    def total(self):
        return self.hourly_rate * self.hours

def calculate_total(item):
    return item.total()

print(f"Product: ${calculate_total(Product(100))}")
print(f"Service: ${calculate_total(Service(50, 3))}")
