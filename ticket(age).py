
# CHECK THE AGE FOR TICKET BOOKING
# USING(nested if)

age=int(input("Enter the age:"))
ticket=input("Did You have Tickets?")
if(ticket=="Yes"):
    if(age>18):
        print("Yor are allowed to watch the match")
    else:
        print("You are not allowed still you got tickets")
else:
    print("You are not allowed")
    
    
