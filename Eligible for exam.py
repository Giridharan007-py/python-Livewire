
# CHECK THE ELIGIBLITY FOR EXAM
# USING (NESTED if)

name=input("Enter the name:")
age=int(input("Enter your age:"))
place=input("Enter your place:")
if(age>=18 and place=="chennai"):
    print("Your eligible to write the exam")
else:
    if(age<18 and place=="chennai"):
        print("Your not eligible to write the exam")
        print("Your are under age")
    elif(age>=18 and place!="chennai"):
        print("Your not eligible to write the exam")
        print("Your are over range")
    else:
        pass
