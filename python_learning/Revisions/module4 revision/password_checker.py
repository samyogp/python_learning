# this is the revision off the password checker in the python module 4

password = "python123"
guess =  input("Enter password: ")
while guess != password:
    print("Wrong password. Try again.")
    guess = input("Enter password: ")
    print("Access granted!")

    