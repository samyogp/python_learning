# nested if example inside if statement 
age = 20 
has_license = True
if age >= 18:
    if has_license:
        print("you can drive!")
    else:
        print("you need a license to drive!")
else:
        print("Too young to drive!")