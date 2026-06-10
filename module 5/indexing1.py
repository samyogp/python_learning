# indexing example using via user input
num_items = input("How many items do you want to add to the list? ")
num_items = int(num_items)
user_list = []
for _ in range(num_items):
    item = input("Enter an item: ")
    user_list.append(item)
print("Your list:", user_list)
# accessing elements in the list using indexing
index = input("Enter the index of the item you want to access (starting from 0): ")
index = int(index)
if 0 <= index < len(user_list):
    print(f"The item at index {index} is: {user_list[index]}")
else:
    print("Invalid index. Please enter a number between 0 and", len(user_list)-1)
    print