# write a program to find the amount for the used current using (function)
'''
unit=int(input("Enter the units to be used:"))
current=''
amount=0
def units():
    print("(A) Normal   (B) Commercial")
    types=input("Enter the type of the current:")
    if(types=="A"):
        current="Normal"
        print("Number of units used:",unit)
        print("The type of the current:",current)
        if(unit<=100):
            amount=unit*2
            print("TOTAL AMOUNT:",amount)
        elif(unit>100 and unit<=200):
            amount=unit*4
            print("TOTAL AMOUNT:",amount)
        else:
            amount=unit*6
            print("TOTAL AMOUNT:",amount)
    elif(types=="B"):
        current="Commercial"
        print("Number of units used:",unit)
        print("The type of the current:",current)
        if(unit<=100):
            amount=unit*4
            print("TOTAL AMOUNT:",amount)
        elif(unit>100 and unit<=200):
            amount=unit*8
            print("TOTAL AMOUNT:",amount)
        else:
            amount=unit*12
            print("TOTAL AMOUNT:",amount)
    else:
        print("Enter a valid type of current")
if(unit<=0):
    print("Enter a valid unit of current")
else:
    units()
'''


# WRITE A PROGRAM TO CHECK THE CURRENT TO BE USED 
'''
tv=5
fan=3
light=2
computer=4
def hour():
    tv_hrs=int(input("Enter the run time of TV (in hours):"))
    fan_hrs=int(input("Enter the run time of FAN (in hours):"))
    light_hrs=int(input("Enter the run time of LIGHT (in hours):"))
    computer_hrs=int(input("Enter the run time of COMPUTER (in hours):"))
    tv_unit=tv*tv_hrs
    fan_unit=fan*fan_hrs
    light_unit=light*light_hrs
    computer_unit=computer*computer_hrs
    unit=tv_unit+fan_unit+light_unit+computer_unit
    def units():
        print("(A) Normal   (B) Commercial")
        types=input("Enter the type of the current:")
        if(types=="A"):
            current="Normal"
            print("Number of units used:",unit)
            print("The type of the current:",current)
            if(unit<=100):
                amount=unit*2
                print("TOTAL AMOUNT:",amount)
            elif(unit>100 and unit<=200):
                amount=unit*4
                print("TOTAL AMOUNT:",amount)
            else:
                amount=unit*6
                print("TOTAL AMOUNT:",amount)
        elif(types=="B"):
            current="Commercial"
            print("Number of units used:",unit)
            print("The type of the current:",current)
            if(unit<=100):
                amount=unit*4
                print("TOTAL AMOUNT:",amount)
            elif(unit>100 and unit<=200):
                amount=unit*8
                print("TOTAL AMOUNT:",amount)
            else:
                amount=unit*12
                print("TOTAL AMOUNT:",amount)
        else:
            print("Enter a valid type of current")
    if(unit<=0):
        print("Enter a valid unit of current")
    else:
        units()
hour()
'''



# WRITE A PROGRAM TO PRINT A STRING AND NUMBER USING CONCADINATE

i=5
number=''
string=''
total=''
t2=''
while(i!=0):
    print("(A)integer   (B)string")
    types=input("Enter the datatype:")
    if(types=="A"):
        number=(input("Enter a number:"))
        string=''
    else:
        string=(input("Enter a string:"))
        number=''
    total=number+string
    t2=t2+total
    i-=1
print(t2)












































