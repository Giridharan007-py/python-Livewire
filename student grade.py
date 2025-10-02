# FIND THE GRADE OF THE STUDENT

name=input("Enter the student name:")
roll_no=int(input("Enter the roll number:"))
school=input("Enter the school name:")
tamil=int(input("Enter TAMIL mark:"))
english=int(input("Enter ENGLISH mark:"))
maths=int(input("Enter MATHS mark:"))
physics=int(input("Enter PHYSICS mark:"))
chemistry=int(input("Enter CHEMISTRY mark:"))
computer=int(input("Enter COMPUTER mark:"))
total=(tamil+english+maths+physics+chemistry+computer)
print("NAME:",name)
print("ROLL NO:",roll_no)
print("SCHOOL NAME:",school)
print("TAMIL mark:",tamil)
print("Enter ENGLISH mark:",english)
print("Enter MATHS mark:",maths)
print("Enter PHYSICS mark:",physics)
print("Enter CHEMISTRY mark:",chemistry)
print("Enter COMPUTER mark:",computer)
if(total>=550):
    print(name,"got A grade")
elif(total<550 and total>=500):
    print(name,"got B grade")
elif(total<500 and total>=450):
    print(name,"got C grade")
else:
    print(name,"got D grade")












