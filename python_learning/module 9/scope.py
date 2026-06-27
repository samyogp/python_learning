# scope.py
x = 10            # Global variable

def my_function():
    y = 5         # Local variable
    print(x)      # Can access global variable
    print(y)      # Can access local variable

my_function()
print(x)          # Works
print(y)          # Error