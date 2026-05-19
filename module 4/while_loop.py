# syntax 
# while condition:
    # code to repeat while condition is true
    # make sure condition becomes false eventually to avoid infinite loop
# example of while loop in python
count = 0
while count <= 13:
    print(count)
    count = count + 1

    # another example of while loop with user input
    number = input("Enter a number:")
    # converting input to int for the calculation 
    number = int(number)
    while number > 0:
        print(number)
        number = number - 1

# 📝 Note: If you forget count += 1, loop runs forever (infinite loop). Press Ctrl+C to stop.
