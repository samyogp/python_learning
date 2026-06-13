# dict_comprehension.py
squares = {x: x*x for x in range(1, 6)}
print(squares)  # {1:1, 2:4, 3:9, 4:16, 5:25}
# user input example
num = int(input("Enter a number: "))
squares = {x: x*x for x in range(1, num+1)}
print(squares)
