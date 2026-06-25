# remove_vowels.py
text = input("Enter a string: ")
vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
result = ''.join([ch for ch in text if ch not in vowels])
print(f"Without vowels: {result}")

# printing hello from user
user_input = input("please enter a any word: ")
print(f"Hello, {user_input}!")
# saying hungry to the waiter in hotel using python code
hungry_input = input("Are you hungry? (yes/no): ")
if hungry_input.lower() == "yes":
    print("The waiter approaches and asks how they can help.")
else:
    print("The waiter nods and moves on.")
    
