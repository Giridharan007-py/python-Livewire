# COLLAGE APPLICATION AND ADMISSION PROCESS

noon=input("Enter the noon:")
time=int(input("Enter the time:"))
print("(A) APPLICATION     (B) ADMISSION")
event=input("Enter the event:")
def app():
    print("Application process is going in the given time")
def adm():
    print("Admission process is going in the given time")
if(noon=="AN" or noon=="FN"):
    if(time<=0):
        print("Enter valid time")
    else:
        if(noon=="FN"):
            if(time>=9 and time<12 and event=="A"):
                app()
            elif(time>=9 and time<12 and event=="B"):
                print("Please come later or wait")
                print("ADMISSION process is held after 3'o clock")
            else:
                print("The collage is closed")
        elif(noon=="AN"):
            if((time==12) or (time>=1 and time<=3) and (event=="A")):
                app()
            elif((time==12) or (time>=1 and time<=3) and (event=="B")):
                print("Please come later or wait")
                print("ADMISSION process is held after 3'o clock")
            elif(time>3 and time<=9 and event=="B"):
                adm()
            elif(time>3 and time<=9 and event=="A"):
                print("SORRY,you came at wrong time")
                print("APPLICATION processes are already done")
            else:
                print("The collage is closed")
else:
    pass



