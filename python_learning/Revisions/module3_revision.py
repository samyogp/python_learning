# this is the revision of the module 3 of python learning in the leap year or not 
year = input("Enter a year: ")
# convert to the integer
year = int(year)

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
    
