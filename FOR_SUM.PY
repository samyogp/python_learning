# sum using for loop

n = input("Enter a number: ")
# converting input to int for the calculation
n = int(n)

total = 0
for i in range(1, n+1):
    total += i
    print(f"Sum = {total}")
