 # SHOP OPEN OR CLOSE 
        
noon=input("Enter the noon:")
time=int(input("Enter a time:"))
if(noon=="AN" or noon=="FN"):
    if(time<=0):
        print("Enter valid time")
    else:
        if(noon=="FN"):
            if(time>=9 and time<12):
                print("The shop is open")
            else:
                print("the shop is closed")
        else:
            if((time==12) or (time>=1 and time<=10)):
                print("The shop is open")
            else:
                print("The shop is closed")
else:
    pass
