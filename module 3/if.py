# if example 
age = 18
if age >= 18:
    print("You can vote!")


    # another example with the user input 
    age = input("Enter your age: ")
    age = int(age)

    if age >= 18:
        print("you can vote!")
    else: 
        print("you cannot vote yet.")


        # another example with user input in if condition
        temprature = input("Enter the temperature in celsius:")
        temprature = float(temprature)
        if temprature > 30:
            print(f"The temperature is {temprature} degree celsius. its a hot day. Drink water!")
            