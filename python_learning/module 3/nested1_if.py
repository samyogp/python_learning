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


        # better way (using and - next topic):
        if age >= 18 and has_license:
             print("You can drive!")
    # common mistake to avoid  mistake 1
    #  if age > 18   # SyntaxError
   # print("ok")     
   # mistake 2
   # if age > 18:
  # print("ok")   # IndentationError
   
   # mistake 3
   # if age = 18:   # SyntaxError (assignment, not comparison)
   # correct way:
  # if age == 18:
  # mistake 4
  #Putting semicolon or extra spaces
 # Just use proper indentation and colon.
     
