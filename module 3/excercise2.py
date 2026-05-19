# check if a year is a leap year or not 
year = input("Enter a year:")
# converting input to integer for the calculation 
year = int(year)

if (year % 4 == 0  and year % 100 != 0) or year % 400 == 0:
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
    