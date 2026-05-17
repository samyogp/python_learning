# modulus % (remainder after division)

print(10 % 3)  # 1 (10 divided by 3 is 3 with a remainder of 1)

print(17 % 5) # 2 (17 divided by 5 is 3 with a remainder of 2)
print(20 % 4)  # 0 (20 divided by 4 is 5 with no remainder)
print(-10 % 3) # 2 ( -10 divided by 3 is -4 with a remainder of 2)


# another example of modulus where user can input the numbers 

num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

# converting the input to float for the calculation 
num1 = float(num1)
num2 = float(num2)


# performing modules operation 
result = num1 % num2
print(f"The result of the modulus of {num1} by {num2} is: {result}")
