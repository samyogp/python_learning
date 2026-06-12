# complete_input_demo.py
print("===== USER REGISTRATION DEMO =====")

# String input (no conversion needed)
full_name = input("Enter your full name: ")

# Integer input with conversion
age = int(input("Enter your age: "))

# Float input
height = float(input("Enter your height in meters: "))

# Boolean – need to convert string to bool manually
is_student_input = input("Are you a student? (yes/no): ")
is_student = is_student_input.lower() == "yes"

# Using the data
print("\n--- Your Information ---")
print(f"Name: {full_name}")
print(f"Age: {age}")
print(f"Height: {height}m")
print(f"Student status: {is_student}")

# Do some calculation
next_birthday_age = age + 1
print(f"On your next birthday, you'll be {next_birthday_age} years old.")