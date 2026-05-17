# // integer division example 

print(10 // 2) # 5 (integer)
print(20 // 6) # 3 (integer, not 3.3333)
print(-10 // 3) # -4 (integer, not -3.3333)


# another example of integer division where user can input the numbers 
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

# converting the input to float for the calculation 
num1 = float(num1)
num2 = float(num2)


# performing integer division 
result = num1 // num2
print(f"The result of the integer division of {num1} by {num2} is: {result}")
