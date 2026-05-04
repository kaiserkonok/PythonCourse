# 🏷️ Instance vs Class Attributes: Who Owns the Data?

<p align="center">
  <img src="https://img.shields.io/badge/Instance-Per%20Object-blue?style=flat-square" alt="instance">
  <img src="https://img.shields.io/badge/Class-Shared%20Data-green?style=flat-square" alt="class">
  <img src="https://img.shields.io/badge/Mutable-Be%20Careful-orange?style=flat-square" alt="Mutable">
</p>

> ### 💡 Instance attributes belong to each object. Class attributes are shared by all objects — like a company name vs an employee ID.
> Learn when to use each type and avoid common pitfalls.

---

## 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- ✅ Define instance and class attributes
- ✅ Understand when to use each type
- ✅ Avoid the mutable class attribute trap

---

## 🧠 Mental Model: A Company

```
🏢 Company (Class)
   ├── 🏢 Name: "TechCorp"     ← Class attribute (shared by all)
   └── 👤 Employees (Objects)
       ├── Alice: ID=1, Salary=80k  ← Instance attributes (unique)
       ├── Bob:   ID=2, Salary=75k  ← Instance attributes (unique)
```

- **Class attributes** = Company-wide info (same for everyone)
- **Instance attributes** = Personal info (unique to each)

---

## 📖 Defining Attributes

```python
class Employee:
    company = "TechCorp"  # Class attribute (shared)

    def __init__(self, name, salary):
        self.name = name       # Instance attribute
        self.salary = salary   # Instance attribute
```

---

## 📊 Instance vs Class

| Feature | Instance Attribute | Class Attribute |
|---------|-------------------|-----------------|
| **Defined in** | `__init__` with `self` | Directly in class body |
| **Scope** | Unique per object | Shared by all objects |
| **Change one** | Only that object changes | All objects see change |
| **Use for** | Unique data (name, age) | Shared constants (company, version) |

---

## ⚠️ Common Mistakes

```
❌ Mutable class attributes (dangerous!)
   class Dog:
       tricks = []  ← Shared list! All dogs share the same list!

   def __init__(self, name):
       self.name = name
       self.tricks.append("sit")  ← Affects ALL dogs!

   ✅ Fix: Use instance attribute
   def __init__(self, name):
       self.tricks = []  ← Each dog has own list

❌ Shadowing class attributes
   obj = MyClass()
   obj.class_attr = "new"  ← Creates instance attribute, shadows class attr
   MyClass.class_attr      ← Still original value

❌ Modifying class attribute via instance
   obj.class_attr += 1  ← Doesn't work for mutable types as expected
```

---

## 💻 Code Examples

### 📌 Example 1 — Instance Attributes

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

alice = Person("Alice", 25)
bob = Person("Bob", 30)

print(alice.name)  # Alice
print(bob.name)    # Bob (different!)
```

### 📌 Example 2 — Class Attributes

```python
class Employee:
    company = "TechCorp"  # Shared by all

    def __init__(self, name):
        self.name = name

e1 = Employee("Alice")
e2 = Employee("Bob")

print(e1.company)  # TechCorp
print(e2.company)  # TechCorp
```

### 📌 Example 3 — Modifying Class Attributes

```python
class Setting:
    theme = "dark"  # Class attribute

s1 = Setting()
s2 = Setting()

# Change via class
Setting.theme = "light"
print(s1.theme)  # light (both affected)
print(s2.theme)  # light
```

### 📌 Example 4 — Counter Pattern

```python
class User:
    user_count = 0  # Class attribute

    def __init__(self, name):
        self.name = name
        User.user_count += 1  # Increment on creation

u1 = User("Alice")
u2 = User("Bob")
u3 = User("Charlie")

print(f"Total users: {User.user_count}")  # 3
```

### 📌 Example 5 — The Mutable Trap

```python
# ❌ Wrong — shared list
class BadTeam:
    members = []  # Shared across ALL instances!

    def __init__(self, name):
        self.name = name
        BadTeam.members.append(name)

t1 = BadTeam("Alice")
t2 = BadTeam("Bob")
print(t1.members)  # ['Alice', 'Bob'] ← Both see all members!

# ✅ Correct — instance list
class GoodTeam:
    def __init__(self, name):
        self.name = name
        self.members = []  # Each team has own list

    def add_member(self, member):
        self.members.append(member)
```

### 📌 Example 6 — Combining Both

```python
class Product:
    tax_rate = 0.08  # Class attribute (shared)

    def __init__(self, name, price):
        self.name = name       # Instance attribute
        self.price = price     # Instance attribute

    def total_price(self):
        return self.price * (1 + Product.tax_rate)

p1 = Product("Laptop", 1000)
p2 = Product("Phone", 500)

print(f"{p1.name}: ${p1.total_price()}")
print(f"{p2.name}: ${p2.total_price()}")
```

---

## 🧪 Practice Exercise

1. Create a class with a class attribute `school_name`
2. Create instances with unique instance attributes
3. Modify the class attribute and see how it affects all instances
4. Create a counter that tracks how many objects were created

---

## 📋 Key Takeaways

| Concept | Takeaway |
|---------|----------|
| 🏷️ **Instance** | Unique to each object — `self.attr` |
| 🏷️ **Class** | Shared by all objects — `ClassName.attr` |
| ⚠️ **Mutable trap** | Never use mutable class attributes (lists, dicts) |
| 🔢 **Counter** | Class attributes are great for tracking instances |
| 🔄 **Shadowing** | Setting `obj.attr` creates an instance attribute |

---

## 🔗 Further Reading

- 📖 [Class and Instance Variables — Official Docs](https://docs.python.org/3/tutorial/classes.html#class-and-instance-variables)
- 🌟 [Class Variables vs Instance — Real Python](https://realpython.com/instance-class-and-static-methods-demystified/)
- 🔧 [Mutable Default Arguments — docs](https://docs.python.org/3/tutorial/classes.html#class-and-instance-variables)