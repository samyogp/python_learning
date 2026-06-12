# list_examples.py
fruits = ["apple", "banana", "mango"]
numbers = [10, 20, 30, 40]
mixed = [1, "hello", 3.14, True]
# An empty list
empty = []

# another example of list with user input
num_items = input("How many items do you want to add to the list?")
num_items = int(num_items)
user_list = []
for _ in range(num_items):
    item = input("Enter an item: ")
    user_list.append(item)
    print(f"Current list: {user_list}")
print(f"Final list: {user_list}")
