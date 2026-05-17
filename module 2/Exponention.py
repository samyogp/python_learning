# exponent example
print(2 ** 3) # 8
print(5 ** 2) # 25
print(10 ** 4) # 10000
print(9 ** 0.5) # 3.0 (square root of 9) 


# another example of exponent where user can input the base and the exponent 
base = input("Enter the base number: ")
exponent = input("Enter the exponent: ")

# converting the input to float for the calculation 
base = float(base)
exponent = float(exponent)

# performing exponentiation

calculation = base ** exponent
print(f"The result of {base} raised to the power of {exponent} is: {calculation}")

