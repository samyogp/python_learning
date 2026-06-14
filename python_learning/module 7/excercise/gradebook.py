# this is the grade book example in python of students and their grades.

students = {}
n= int(input("Enter the number of students:  "))
for i in range(n):
    name = input("Name: ")
    grade = input("Grade: ")
    #converting grade to float
    students[name] = float(grade)

    average = sum(students.values()) / len(students)
    print(f"\nClass average: {average:.2f}")
    for name, grade in students.items():
        status = "pass" if grade >= 40 else "fail"
        print(f"{name}: {grade} - {status}")
        