
# FIND THE AMUONT FOR THE UNIT OF CURRENT USED
# USING (if,elif,else)          

unit=int(input("Enter the total units:"))
amount=int()
if(unit<0):
    print("Enter a valid units")
else:
    if(unit>=0 and unit<=100):
        amount=unit*1
        print("AMOUNT:",amount)
    elif(unit>100 and unit<=200):
        amount=unit*2
        print("AMOUNT:",amount)
    elif(unit>200):
        commercial=input("If it is commercial ?")
        if(commercial=="yes"):
            amount=unit*12
            print("AMOUNT:",amount)
        else:
            amount=unit*4
            print("AMOUNT:",amount)
    else:
        pass
