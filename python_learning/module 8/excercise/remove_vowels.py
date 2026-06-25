# remove_vowels.py
text = input("Enter a string: ")
vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
result = ''.join([ch for ch in text if ch not in vowels])
print(f"Without vowels: {result}")

# printing hello from user
user_input = input("please enter a any word: ")
print(f"Hello, {user_input}!")
