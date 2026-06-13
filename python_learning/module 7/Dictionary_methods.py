person = {"name": "samyog", "age": 19, "job": "Engineer"}

# print dictionary methods
print(person.keys())
print(person.values())
print(person.items())

print("\n--- Looping keys ---")
for key in person.keys():
    print(f"key: {key}: {person[key]}")

print("\n--- Looping items (better way) ---")
for key, value in person.items():
    print(f"key: {key}: {value}")

# update outside loop
person.update({"city": "lalitpur", "age": 20})

print("\n--- Updated dictionary ---")
print(person)