# Inheritance: Creating Hierarchies

## Learning Objectives

- Understand inheritance
- Create parent and child classes
- Use super() to access parent methods

## What is Inheritance?

Inheritance allows a class to **inherit attributes and methods** from another class:

- **Parent class** (base) - the original
- **Child class** (derived) - inherits from parent

```python
class Animal:  # Parent
    def speak(self):
        return "Some sound"

class Dog(Animal):  # Child
    pass

dog = Dog()
print(dog.speak())  # "Some sound" - inherited!
```

## Creating Child Classes

```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.speak())  # Woof!
print(cat.speak())  # Meow!
print(dog.name)     # Buddy (inherited!)
```

## Using super()

`super()` accesses the parent class:

```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call parent's __init__
        self.breed = breed  # Add new attribute

dog = Dog("Buddy", "Labrador")
print(dog.name)  # Buddy (from parent)
print(dog.breed) # Labrador
```

## Code Examples

```python
# Example 1: Simple inheritance
class Vehicle:
    def drive(self):
        return " Driving"

class Car(Vehicle):
    pass

car = Car()
print(car.drive())  # Driving (inherited)

# Example 2: Override method
class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

print(Dog().speak())  # Woof!
print(Cat().speak())  # Meow!

# Example 3: Extend parent method
class Shape:
    def draw(self):
        return "Drawing shape"

class Circle(Shape):
    def draw(self):
        return super().draw() + " - Circle"

print(Circle().draw())  # Drawing shape - Circle

# Example 4: Multi-level inheritance
class LivingThing:
    def breathe(self):
        return "Breathing"

class Animal(LivingThing):
    def move(self):
        return "Moving"

class Dog(Animal):
    def bark(self):
        return "Barking"

dog = Dog()
print(dog.breathe())  # Breathing (from LivingThing)
print(dog.move())    # Moving (from Animal)
print(dog.bark())   # Barking (own)

# Example 5: Multiple attributes
class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def __init__(self, name, id):
        super().__init__(name)
        self.id = id

emp = Employee("Alice", 123)
print(emp.name)  # Alice
print(emp.id)    # 123
```

## When to Use Inheritance

- **Is-a relationship**: Dog is an Animal
- **Code reuse**: Don't repeat code
- **Common interface**: Same methods

## Key Takeaways

1. **Parent class** - provides attributes/methods
2. **Child class** - inherits from parent
3. **Override** - replace parent method
4. **super()** - access parent methods
5. **Multi-level** - chain of inheritance

## Practice Exercise

1. Create a parent class Vehicle with drive() method
2. Create Car child that inherits from Vehicle
3. Override drive() in Car
4. Create a child with extended __init__