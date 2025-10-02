
# CHECK THE ELIGIBLITY FOR VOTE
# USING (NESTED if)

age=int(input("Enter the age:"))
if(age<18 or age>120):
    print("Enter a valid age")
else:
    voter_id=input("Did you have a VOTER ID ?")
    if(age>=18 and voter_id=="yes"):
        print("Your are eligible to vote")
    else:
        if(age<18 and voter_id=="yes"):
            print("Your are not eligible to vote")
            print("YOU ARE UNDER AGE")
        elif(age>=18 and voter_id=="no"):
            print("Your are not eligible to vote")
            print("GET YOUR VOTER ID FIRST !")
        else:
            pass

        
    



































    




























