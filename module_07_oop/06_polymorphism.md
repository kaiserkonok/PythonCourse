# Polymorphism: Method Overriding and Flexibility

## Learning Objectives

- Understand polymorphism
- Use method overriding
- Create flexible code with polymorphism

## What is Polymorphism?

Polymorphism means **"many forms"**:

- Same method, different behavior
- Child classes override parent methods
- More flexible and extensible code

```python
class Animal:
    def speak(self):
        pass  # Placeholder

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Same interface, different behavior
animals = [Dog(), Cat()]
for animal in animals:
    print(animal.speak())  # Woof! Meow!
```

## Method Overriding

Child class provides its own version:

```python
class Shape:
    def area(self):
        return 0

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):  # Override
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):  # Override
        return self.side ** 2
```

## Using Polymorphism

```python
def print_area(shape):
    print(f"Area: {shape.area()}")

circle = Circle(5)
square = Square(4)

print_area(circle)  # 78.5
print_area(square)  # 16
```

## Code Examples

```python
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

# Example 3: Override with super()
class Bird:
    def fly(self):
        return "Flying"

class Penguin(Bird):
    def fly(self):
        return "Can't fly :("

p = Penguin()
print(p.fly())  # Can't fly :(

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
```

## Why Use Polymorphism?

| Benefit | Example |
|---------|----------|
| Flexibility | Same code, different behavior |
| Extensibility | Add new classes without changing |
| Clean code | Avoid long if/elif chains |
| Maintainability | Code is easier to modify |

## Key Takeaways

1. **Polymorphism** - same method, different forms
2. **Override** - child replaces parent method
3. **Flexible functions** - work with any type
4. **Best practice** - use common interface
5. **Duck typing** - if it looks like a duck...

## Practice Exercise

1. Create Shape class with area() returning 0
2. Create Circle and Square that override area()
3. Create a function that takes any shape
4. Test with different shapes