# simple calculator using if - elif
a = input("Enter a first number: ")
b = input("Enter a second number: ")
op = input("Operation (+, -, *, /): ")

# converting the input to float for the calculation
a = float(a)
b = float(b)
if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    if b != 0:
        print(a / b)
    else:
        print("cannot divide by zero")
else:
   print("invalid operator")

