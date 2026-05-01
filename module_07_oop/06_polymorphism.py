# Code examples from "Polymorphism" lesson

# Example 1: Basic polymorphism
class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

animals = [Dog(), Cat()]
for animal in animals:
    print(animal.speak())

print("---")

# Example 2: Function with polymorphism
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height

def print_area(shape):
    print(f"Area: {shape.area()}")

print_area(Rectangle(4, 5))  # 20
print_area(Triangle(4, 5))  # 10

print("---")

# Example 3: Override with super()
class Bird:
    def fly(self):
        return "Flying"

class Penguin(Bird):
    def fly(self):
        return "Can't fly :("

p = Penguin()
print(p.fly())  # Can't fly :(

print("---")

# Example 4: Abstract-like behavior
class User:
    def login(self):
        pass

class Admin(User):
    def login(self):
        return "Admin login: full access"

class RegularUser(User):
    def login(self):
        return "User login: limited access"

users = [Admin(), RegularUser()]
for user in users:
    print(user.login())

print("---")

# Example 5: Using isinstance
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

def make_speak(animal):
    if isinstance(animal, Dog):
        return "Dog says: " + animal.speak()
    elif isinstance(animal, Cat):
        return "Cat says: " + animal.speak()
    return "Unknown"

print(make_speak(Dog()))
print(make_speak(Cat()))


# =====================
# PRACTICE EXERCISE
# =====================

# 1. Create Shape class with area() returning 0
class Shape:
    def area(self):
        return 0

# 2. Create Circle and Square that override area()
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side ** 2

# 3. Create a function that takes any shape
def get_area(shape):
    return shape.area()

# 4. Test with different shapes
shapes = [Circle(5), Square(4), Shape()]
for shape in shapes:
    print(f"Area: {get_area(shape)}")