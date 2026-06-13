# task : Ask the user for length & width, calculate area of rectangle.
length = input("Enter the length of the rectangle: ")
width = input("Enter the width of the rectangle: ")
# converting to input to float for calculation 
float_length = float(length)
float_width = float(width)

area = float_length * float_width
print(f"The area of the rectangle is: {area}")
