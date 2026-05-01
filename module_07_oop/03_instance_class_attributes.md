# Instance vs Class Attributes: Data That Belongs to an Object vs the Whole Class

## Learning Objectives

- Distinguish between instance and class attributes
- Use class attributes for shared data
- Access both types correctly

## Instance vs Class Attributes

| Type | Belongs to | Created | Use case |
|------|-----------|---------|----------|
| Instance | Individual object | Each object | Unique data |
| Class | Whole class | Class definition | Shared data |

```python
class Dog:
    # Class attribute - shared by all dogs
    species = "Canis familiaris"
    
    def __init__(self, name):
        # Instance attribute - unique to each dog
        self.name = name
```

## Class Attributes

```python
class Dog:
    species = "Canis familiaris"  # Shared by all
    
    def __init__(self, name):
        self.name = name

dog1 = Dog("Buddy")
dog2 = Dog("Max")

print(dog1.species)  # Canis familiaris
print(dog2.species)  # Canis familiaris

# Can also access via class
print(Dog.species)  # Canis familiaris
```

## Instance Attributes

```python
class Person:
    def __init__(self, name):
        self.name = name  # Instance attribute

person1 = Person("Alice")
person2 = Person("Bob")

print(person1.name)  # Alice
print(person2.name)  # Bob
```

## Modifying Class Attributes

```python
class Company:
    employee_count = 0  # Class attribute
    
    def __init__(self, name):
        self.name = name  # Instance attribute
        Company.employee_count += 1

emp1 = Company("Alice")
emp2 = Company("Bob")

print(Company.employee_count)  # 2
```

## Code Examples

```python
# Example 1: Instance attributes
class Car:
    def __init__(self, brand):
        self.brand = brand

car1 = Car("Toyota")
car2 = Car("Honda")
print(car1.brand)  # Toyota
print(car2.brand)  # Honda

# Example 2: Class attributes
class Animal:
    kingdom = "Animalia"  # Same for all

print(Animal.kingdom)
a1 = Animal()
a2 = Animal()
print(a1.kingdom)  # Same value for both

# Example 3: Mixed
class Student:
    school = "Python High"  # Class attribute
    
    def __init__(self, name, grade):
        self.name = name    # Instance
        self.grade = grade  # Instance

s1 = Student("Alice", "A")
s2 = Student("Bob", "B")
print(s1.school)  # Python High
print(s2.school)  # Python High

# Example 4: Counter using class attribute
class Counter:
    count = 0
    
    def __init__(self):
        Counter.count += 1
    
    def get_count(self):
        return Counter.count

c1 = Counter()
c2 = Counter()
c3 = Counter()
print(f"Count: {Counter.count}")  # 3

# Example 5: Default values with class attribute
class Database:
    connection_timeout = 30  # Default
    
    def __init__(self, host):
        self.host = host

db1 = Database("localhost")
print(db1.connection_timeout)  # 30 (default)
db2 = Database("server")
print(db2.connection_timeout)  # 30 (default)
```

## Best Practices

- **Class attributes** for constants and defaults
- **Instance attributes** for unique data
- **Access** via self or class name
- **Modify class** via ClassName.attribute

## Key Takeaways

1. **Instance** - unique per object (self.attr)
2. **Class** - shared by all (Class.attr)
3. **Modify class** - affects all
4. **Modify instance** - affects only one
5. **Common use** - counters, constants, defaults

## Practice Exercise

1. Create a class with a class attribute (species)
2. Create instances with instance attributes
3. Modify class attribute and see effect
4. Create a counter using class attribute