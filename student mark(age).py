
# CHECK THE AGE FOR PRINT THE MARK OF THE STUDENT
# USING(nested if)

name=input("Enter the student name:")
age=int(input("Enter the age:"))
roll_no=int(input("Enter the roll number:"))
tamil=int(input("Enter TAMIL mark:"))
english=int(input("Enter ENGLISH mark:"))
maths=int(input("Enter MATHS mark:"))
physics=int(input("Enter PHYSICS mark:"))
chemistry=int(input("Enter CHEMISTRY mark:"))
computer=int(input("Enter COMPUTER mark:"))
total=(tamil+english+maths+physics+chemistry+computer)
average=total/6
print("NAME:",name)
print("ROLL NO:",roll_no)
if(age<=18):
    if(tamil>=35 and english>=35 and maths>=35 and physics>=35 and chemistry>=35 and computer>=35):
        print("TOTAL:",total)
        print("AVERAGE:",average)
        print("You have passed")
    else:
        print("You failed")
else:
    print("You are over aged")
'''













