'''
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
print("TOTAL:",total)
if(tamil>=45 and english>=45 and maths>=45 and physics>=45 and chemistry>=4 and computer>=45):
    print("You have passed")
else:
    print("You failed")
    

# ACCOUNT LOG IN

user_name=input("Enter user name:")
password=input("Enter password:")
if(user_name=="admin1234" and password!="1234"):
    print("Enter a valid password")
elif(user_name!="admin1234" and password=="1234"):
    print("Enter a valid user name")
elif(user_name!="admin1234" and password!="1234"):
    print("something went wrong")
else:
    print("You have logged in")

# SHOP OPEN OR CLOSE

time=int(input("Enter a time:"))
if(time>=9 and time<=22):
    print("The shop is open")
else:
    print("the shop is closed")

# ATM (Nested if else)


total=10000
cash=int(input("Enter the amount:"))
balance=total-cash
if(cash<=total):
    if(cash%100==0):
        print("cash debited")
        print("BALANCE:",balance)
    else:
        print("This ATM has only 100 rupees")
elif(cash>total):
    print("insufficient cash")
    print("BALANCE:",total)
else:
    print("SORRY, something went wrong")
'''
# ATM (if,elif,else)
'''
total=20000
cash=int(input("Enter the amount:"))
balance=total-cash
if(cash<=total and cash%100==0):
    print("cash debited")
    print("BALANCE:",balance)
elif(cash<=total and cash%100!=0):
    print("This ATM has only 100 rupee notes")
elif(cash>total):
    print("insufficient cash")
    print("BALANCE:",total)
else:
    print("SORRY, something went wrong. please try again")
'''
# POSITIVE OR NEGATIVE
'''
a=int(input("Enter a number:"))
if( a!=0 and a>0):
    print("The given number is positive")
elif(a!=0 and a<0):
    print("The given number is negative")
else:
    print("The given number is zero")
'''
# 

a=input("Enter a number:")
b=(a[-2])
print("the ten's place of given number:",b)

# vowels
'''
letter=input("Enter a letter:")
if(letter=="A" or letter== "E" or letter=="I" or letter=="O" or letter=="U" or letter=="a" or letter=="e" or letter=="i" or letter=="o" or letter=="u"):
    print("The given letter is VOWEL")
else:
    print("The given letter is CONSONENT")
'''
# SWAPCASE
'''
string=input("Enter a string:")
if(string.isupper()):
    print(string.lower())
elif(string.islower()):
    print(string.upper())
else:
    print(string.swapcase())

# REVERSE THE NUMBER

a=int(input("Enter a number:"))
b=a%10
c=a//10
d=c%10
e=c//10
print("The reversed number:",b,d,e,sep="")

# TEN'S PLACE

a=int(input("Enter a number:"))
b=a//10
c=b%10
print("the ten's place of given number:",c)

'''































































