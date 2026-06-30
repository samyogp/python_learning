# this is the example of the while sum in the python 
n = int(input("Enter a number: "))
total = 0
i = 1
while i <= n:
    total = total + i
    i += 1
    print(f"Sum of 1 to {n} is: {total}")
    