# Code examples from "Inheritance" lesson

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


# =====================
# PRACTICE EXERCISE
# =====================

# 1. Create a parent class Vehicle with drive() method
class Vehicle:
    def drive(self):
        return "Vehicle is driving"

# 2. Create Car child that inherits from Vehicle
class Car(Vehicle):
    pass

car = Car()
print(car.drive())  # Vehicle is driving (inherited)

# 3. Override drive() in Car
class SportsCar(Vehicle):
    def drive(self):
        return "Sports car zooming!"

sports_car = SportsCar()
print(sports_car.drive())  # Sports car zooming!

# 4. Create a child with extended __init__
class ElectricCar(Vehicle):
    def __init__(self, brand, battery_range):
        super().__init__()  # Initialize parent
        self.brand = brand
        self.battery_range = battery_range
    
    def drive(self):
        return f"{self.brand} is driving silently for {self.battery_range} miles"

tesla = ElectricCar("Tesla", 300)
print(tesla.drive())