# indexing example using via user input
num_items = input("How many items do you want to add to the list? ")
num_items = int(num_items)
user_list = []
for _ in range(num_items):
    item = input("Enter an item: ")
    user_list.append(item)
# accessing elements using positive indexing
print(fruits[0])  # output apple
print(fruits[2])  # output will be mango
# accessing elements using negative indexing
print(user_list[-1])  # output will be the last item added
print(user_list[-3]) # output will be the third last item added