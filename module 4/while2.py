# sum of numbers from 1 to user input number using while loop
n = input("Enter a number: ")
# converting input to int for the calculation
n = int(n)
total = 0
i = 1
while i <= n:
    total = total + i
    i += 1
    print(f"sum of 1 to {n} is: {total}")
    