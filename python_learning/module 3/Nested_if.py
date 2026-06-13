# nested if example inside if statement 
age = input("Enter your age: ")
age = int(age)
if age >= 18:
    print(" You can vote!")
    # nested if statement 
    citizenship = input("Enter your citizenship: ")
    if citizenship.lower() == "american":
        print("you are eligible to vote in the US!")
    else:
        print("you are not eligible to vote in the US!")
else:
   print("you cannot vote yet.")
