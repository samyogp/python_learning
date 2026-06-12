# syntax of the else statement in python 
# if condition:
    # code to run if condition is true
# else:
    #code to run if condition is false
# else example
number = input("Enter a number: ")
# converting input to int for the calculation 
number = int(number)

if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")
    