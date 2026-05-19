# grading system using else if statement in python 
# syntax of else if statement in python 
 # if condition1:
        # condition1 true code
    # elseif condition2:
        # condition1 false, condition2 true
    #elseif condition3:
        # both above false, condition3 true
# else:
    # all condition false 

# example of grading system using elseif in python
score = input("Enter your score: ")
# converting to the input to int for the calculation 
score = int(score)

if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
elif score >= 60:
    print("Grade D")
else:
    grade = "F"
    print(f"your grade is {grade}. Better luck next  time!")



