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
cut_off=(physics+chemistry)/2+maths
collage_wanted=""
collage=""
def cutoff():
    if (cut_off>=190 and cut_off<=200):
        print("Congratulations! You have met the cut-off mark for admission")
        print("(A)AVC   (B)SRM   (C)CIT    (D)GCT")
        collage=input("Enter the collage you want:")
    elif(cut_off>=170 and cut_off<=189):
        print("Congratulations! You have met the cut-off mark for admission")
        print("(A)AVC   (B)SRM    (C)CIT")
        collage=input("Enter the collage you want:")
    elif(cut_off>=150 and cut_off<=169):
        print("Congratulations! You have met the cut-off mark for admission")
        print("(A)AVC   (B)SRM")
        collage=input("Enter the collage you want")
    else:
        return "Sorry, you did not meet the cut-off mark for admission."
if(collage=="A"):
    collage_wanted="AVC"
elif(collage=="B"):
    collage_wanted="SRM"
elif(collage=="C"):
    collage_wanted="CIT"
else:
    collage_wanted="GCT"
cutoff()
print("NAME:",name)
print("TOTAL:",total)
print("AVERAGE:",average)
print("CUT OFF:",cut_off)
print("collage joined:",collage_wanted)




