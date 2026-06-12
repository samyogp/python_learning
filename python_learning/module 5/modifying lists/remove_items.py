# removed items in modifying lists using remove and pop and del
# using remove to remove an list item by value.
fruits = ["apple", "banana", "mango", "banana"] 
fruits.remove("banana") # removes first banana only
print(fruits)  # ['apple' , 'mango' , 'banana']

# pop(index) removes and returns item at index (default last )
last = fruits.pop()    # removes and returns 'banana'
print(last) # banana
print(fruits)  # ['apple, mango]

# using del
del fruits[0]
print(fruits)
 
