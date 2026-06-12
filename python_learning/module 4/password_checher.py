# password checker (until correct )

password = "python123"
guess = input("Enter the password: ")
while guess != password:
    print("Incorrect password. Try again.")
    guess = input("Enter the password: ")
    print("Access granted!")
    