# creating simple calculator using if elif

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Operation (+, -, *, /): ")

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    print(a / b)
else:
    print("Invalid operation")
    