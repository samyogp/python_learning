# Exercise 1: Positive, negative, or zero
num = input("Enter a number:")
# converting input to float for the calculation 
num = float(num)

if num > 0:
    print(f"{num} is a positive number.")
elif num < 0:
    print(f"{num} is a negative number.")
else:
    print(f"{num} is zero.")