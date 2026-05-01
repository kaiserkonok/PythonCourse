# Code examples from "Dictionaries" lesson

# Example 1: Create and access
car = {"brand": "Toyota", "model": "Camry", "year": 2022}
print(car["brand"])  # Toyota
print(car.get("year"))  # 2022

# Example 2: Update dictionary
car["year"] = 2023
car["color"] = "blue"
print(car)  # {'brand': 'Toyota', 'model': 'Camry', 'year': 2023, 'color': 'blue'}

# Example 3: Get all keys/values
user = {"name": "Alice", "age": 25, "city": "NYC"}
print(user.keys())    # dict_keys(['name', 'age', 'city'])
print(user.values()) # dict_values(['Alice', 25, 'NYC'])
print(user.items())  # dict_items([('name', 'Alice'), ...])

# Example 4: Loop through dictionary
for key in user:
    print(f"{key}: {user[key]}")

# Example 5: Nested dictionary
company = {
    "employee": {
        "name": "Alice",
        "role": "Developer"
    }
}
print(company["employee"]["name"])  # Alice


# =====================
# PRACTICE EXERCISE
# =====================

# 1. Create a dictionary with your info (name, age, hobby)
my_info = {
    "name": "Alice",
    "age": 25,
    "hobby": "reading"
}

print(f"My info: {my_info}")

# 2. Add a new key
my_info["city"] = "New York"
print(f"After adding city: {my_info}")

# 3. Loop through and print all key-value pairs
print("\nAll key-value pairs:")
for key, value in my_info.items():
    print(f"  {key}: {value}")

# 4. Use .get() with a default value
print(f"\nMissing key: {my_info.get('job', 'Not specified')}")