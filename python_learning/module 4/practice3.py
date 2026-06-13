# factorial using for loop
n = input("Enter a number: ")
# converting input to int for the calculation
n = int(n)
fact = 1
for i in range(1, n+1):
    fact *= i
print(f"{n}! = {fact}")
