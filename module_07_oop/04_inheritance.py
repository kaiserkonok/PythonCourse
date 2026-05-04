"""
Inheritance (Reusing and Extending Classes)
────────────────────────────────────────────────────────────────────────────
Code examples and practice exercises from the lesson.
────────────────────────────────────────────────────────────────────────────
"""

# Example 1 — Basic Inheritance
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

dog = Dog("Buddy")
cat = Cat("Whiskers")

print(f"{dog.name}: {dog.speak()}")
print(f"{cat.name}: {cat.speak()}")


# Example 2 — Using super()
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)  # Call parent constructor
        self.team_size = team_size

m = Manager("Alice", 90000, 5)
print(f"{m.name}: ${m.salary}, manages {m.team_size}")


# Example 3 — Method Overriding
class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):  # Override
        return self.w * self.h

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):  # Override
        return 3.14 * self.r ** 2

print(f"Rectangle: {Rectangle(5, 3).area()}")
print(f"Circle: {Circle(4).area()}")


# Example 4 — Extending Methods
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def info(self):
        return f"Brand: {self.brand}"

class Car(Vehicle):
    def __init__(self, brand, doors):
        super().__init__(brand)
        self.doors = doors

    def info(self):  # Extend parent method
        base = super().info()
        return f"{base}, Doors: {self.doors}"

car = Car("Tesla", 4)
print(car.info())


# Example 5 — isinstance() and issubclass()
class AnimalType: pass
class DogType(AnimalType): pass
class CatType(AnimalType): pass

dog = DogType()

print(isinstance(dog, DogType))     # True
print(isinstance(dog, AnimalType))  # True (Dog IS-A Animal)
print(isinstance(dog, CatType))     # False

print(issubclass(DogType, AnimalType))  # True
print(issubclass(AnimalType, DogType))  # False


# Example 6 — Multiple Inheritance
class Flyer:
    def fly(self):
        return "Flying..."

class Swimmer:
    def swim(self):
        return "Swimming..."

class Duck(Flyer, Swimmer):
    def quack(self):
        return "Quack!"

duck = Duck()
print(duck.fly())   # Flying...
print(duck.swim())  # Swimming...
print(duck.quack()) # Quack!


# ═══════════════════════════════════════════════════════════════════════════════
# PRACTICE EXERCISE
# ═══════════════════════════════════════════════════════════════════════════════
# 1. Create a Vehicle base class with brand and speed
# 2. Create Car and Bike child classes
# 3. Override a method in each child
# 4. Use super() to extend functionality
# ═══════════════════════════════════════════════════════════════════════════════

class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def info(self):
        return f"{self.brand} ({self.speed} km/h)"

class Car(Vehicle):
    def __init__(self, brand, speed, seats):
        super().__init__(brand, speed)
        self.seats = seats

    def info(self):
        return f"{super().info()}, {self.seats} seats"

class Bike(Vehicle):
    def __init__(self, brand, speed, has_basket):
        super().__init__(brand, speed)
        self.has_basket = has_basket

    def info(self):
        basket = "with basket" if self.has_basket else "no basket"
        return f"{super().info()}, {basket}"

c = Car("Tesla", 200, 5)
b = Bike("Trek", 30, True)

print(c.info())
print(b.info())

# Try modifying it:
# - Create a hierarchy with 3 levels
class Person:
    def __init__(self, name):
        self.name = name

class Employee2(Person):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

class Manager2(Employee2):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def info(self):
        return f"{self.name}: ${self.salary}, manages {self.team_size}"

mgr = Manager2("Alice", 100000, 8)
print(mgr.info())
