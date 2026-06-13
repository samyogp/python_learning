# this is the checking if key exist in operator

# in_dict.py
inventory = {"apples": 10, "bananas": 5}
if "apples" in inventory:
    print(f"We have {inventory['apples']} apples")

    # user input example
    stock = {"apples": 10, "bananas": 5, "oranges": 8}
    fruit = input("Enter a fruit to check: ")
    if fruit in stock:
        print(f"We have {stock[fruit]} {fruit}")
    else: 
        print(f"Sorry, we don't have {fruit}")
        